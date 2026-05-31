# 🛡️ AI Privacy Shield
### Intelligent Shoulder Surfing Protection System

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Flask](https://img.shields.io/badge/Flask-Latest-green)
![OpenCV](https://img.shields.io/badge/OpenCV-Latest-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 Problem Statement
In public spaces like offices, cafes, libraries, and classrooms, laptop users are constantly exposed to **shoulder surfing** — where unauthorized individuals view sensitive information directly from a screen. Existing solutions like physical privacy filters are static, inconvenient, and non-intelligent.

---

## 💡 Solution
AI Privacy Shield is an intelligent, real-time privacy protection system that:
- 👁️ Monitors surroundings using laptop webcam
- 🤖 Detects unauthorized viewers using Computer Vision
- 🌫️ Automatically blurs screen when threat detected
- ⏱️ Gives 5-second countdown warning
- 🔒 Locks screen if threat persists
- 🛡️ Runs silently in system tray — one click activation

---

## ✨ Features
- ✅ Real-time face detection
- ✅ SAFE / ALERT status dashboard
- ✅ Gradual screen blur overlay
- ✅ Auto screen lock after 5 seconds
- ✅ System tray icon — background protection
- ✅ Live dashboard — updates every 2 seconds
- ✅ False detection prevention using averaging

---

## 🛠️ Tech Stack
| Technology | Purpose |
|---|---|
| Python 3.14 | Core Logic |
| OpenCV | Face Detection |
| Flask | Backend API |
| HTML/CSS/JS | Frontend Dashboard |
| Tkinter | Blur Overlay |
| PyAutoGUI | Screen Capture |
| Pystray | System Tray Icon |
| Pillow | Image Processing |
| Gemini CLI | AI-assisted Development |

---

## 🚀 How It Works
Webcam ON → Face Detection → 1 Face = SAFE ✅
→ 2+ Faces = ALERT 🔴
→ Screen Blurs 🌫️
→ 5s Countdown ⏱️
→ Screen Lock 🔒

---

## 📦 Installation

### Prerequisites
- Python 3.x
- Webcam

### Setup
```bash
# Clone the repository
git clone https://github.com/SyedaJuveriya/ai-privacy-shield.git

# Navigate to project
cd ai-privacy-shield

# Install dependencies
pip install opencv-python flask pyautogui pillow pystray

# Run dashboard directly
python app.py

# OR Run system tray app
python tray.py
```

---

## 🖥️ Usage

### Option 1 — Direct Dashboard
```bash
python app.py
```
Open browser → `http://127.0.0.1:5000`

### Option 2 — System Tray (Recommended)
```bash
python tray.py
```
- Shield icon appears in taskbar
- Right click → **Start Protection**
- Dashboard opens automatically

---

## 📸 Screenshots

| SAFE State | ALERT State |
|---|---|
| <img width="1917" height="946" alt="image" src="https://github.com/user-attachments/assets/381be9cd-edbb-4fc3-a668-89d7761efc6d" />
 | <img width="1842" height="773" alt="Screenshot 2026-05-21 142002" src="https://github.com/user-attachments/assets/9030f0bd-d7c8-4b08-82e8-7a37600c74ed" />
 |

---

## 🔮 Future Scope
- 🤖 YOLO deep learning model for better accuracy
- 📱 Mobile app — phone notifications
- ☁️ Cloud deployment for enterprise
- 🎭 Mask & side-profile detection  
- 🔊 Audio alerts + Email notifications
- 📊 Alert history & analytics dashboard

---

## 👩‍💻 Developer
**Syeda Juveriya**
B.Tech AI & Data Science — III Year
Shadan Women's College of Engineering & Technology
Hyderabad, India

---

## 🏆 Built For
Hackathon Project — AI Privacy Shield
Built using **Gemini CLI** + **Claude AI** as development tools

---

*"Your AI Bodyguard for Digital Privacy"* 🛡️
