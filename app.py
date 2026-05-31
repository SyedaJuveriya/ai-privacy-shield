from flask import Flask, jsonify, render_template
import cv2
import threading
import ctypes
import time
import pyautogui
import tkinter as tk
from PIL import Image, ImageFilter, ImageTk

app = Flask(__name__)

face_count = 0
status = "SAFE"
alert_start_time = None
blur_window = None

def show_blur_overlay(initial_img):
    global blur_window
    root = tk.Tk()
    blur_window = root
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.config(cursor="none")
    label = tk.Label(root, bg='black')
    label.pack(expand=True, fill='both')

    def update_animation():
        if alert_start_time is not None:
            elapsed = time.time() - alert_start_time
            radius = min(50, (elapsed / 5) * 50)
            blurred = initial_img.filter(
                ImageFilter.GaussianBlur(radius=radius)
            )
            photo = ImageTk.PhotoImage(blurred)
            label.config(image=photo)
            label.image = photo
            root.after(100, update_animation)
        else:
            root.destroy()

    update_animation()
    root.mainloop()

def reset_privacy_shield():
    global alert_start_time, blur_window
    alert_start_time = None
    if blur_window:
        try:
            blur_window.after(0, blur_window.destroy)
        except:
            pass
        blur_window = None

def detect_faces():
    global face_count, status, alert_start_time

    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )
    counts = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Blur active hai toh detection pause karo
        if alert_start_time is not None:
            elapsed = time.time() - alert_start_time
            remaining = max(0, 5 - int(elapsed))
            status = f"ALERT - Locking in {remaining}s!"

            if elapsed >= 5:
                reset_privacy_shield()  # pehle blur band karo
                time.sleep(0.5)
                ctypes.windll.user32.LockWorkStation()  # phir lock
                face_count = 0
                status = "LOCKED"
                time.sleep(3)
                counts.clear()
                face_count = 0
                status = "SAFE"

            time.sleep(0.1)
            continue

        small = cv2.resize(frame, (640, 480))
        gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        faces = face_cascade.detectMultiScale(
            gray, 1.3, 6, minSize=(80, 80)
        )

        counts.append(len(faces))
        if len(counts) > 5:
            counts.pop(0)
        face_count = round(sum(counts) / len(counts))

        if face_count > 1:
            if alert_start_time is None:
                alert_start_time = time.time()
                screen_img = pyautogui.screenshot()
                threading.Thread(
                    target=show_blur_overlay,
                    args=(screen_img,),
                    daemon=True
                ).start()
        else:
            if alert_start_time is not None:
                reset_privacy_shield()
            if face_count == 1:
                status = "SAFE"
            else:
                status = "No Face Detected"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/status')
def get_status():
    return jsonify({
        'face_count': face_count,
        'status': status
    })

if __name__ == '__main__':
    t = threading.Thread(target=detect_faces, daemon=True)
    t.start()
    app.run(debug=False, port=5000)