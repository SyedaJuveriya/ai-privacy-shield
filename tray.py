import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw
import threading
import subprocess
import sys
import os

# Flask app process
flask_process = None

def create_icon():
    # Shield icon banana
    img = Image.new('RGB', (64, 64), color='black')
    draw = ImageDraw.Draw(img)
    # Shield shape
    draw.polygon([
        (32, 4), (60, 16), (60, 36),
        (32, 60), (4, 36), (4, 16)
    ], fill='cyan', outline='white')
    draw.text((22, 24), "AI", fill='black')
    return img

def start_protection(icon, item):
    global flask_process
    if flask_process is None:
        icon.notify("AI Privacy Shield", "Protection Started! 🛡️")
        flask_process = subprocess.Popen(
    [sys.executable, 'app.py'],
    cwd=os.path.dirname(os.path.abspath(__file__)),
    creationflags=subprocess.CREATE_NEW_CONSOLE
        )
        # Update menu
        icon.menu = pystray.Menu(
            pystray.MenuItem("🛡️ Protection: ON", None, enabled=False),
            pystray.MenuItem("⏹️ Stop Protection", stop_protection),
            pystray.MenuItem("❌ Exit", exit_app)
        )

def stop_protection(icon, item):
    global flask_process
    if flask_process:
        flask_process.terminate()
        flask_process = None
        icon.notify("AI Privacy Shield", "Protection Stopped! ⚠️")
        icon.menu = pystray.Menu(
            pystray.MenuItem("🛡️ Protection: OFF", None, enabled=False),
            pystray.MenuItem("▶️ Start Protection", start_protection),
            pystray.MenuItem("❌ Exit", exit_app)
        )

def exit_app(icon, item):
    global flask_process
    if flask_process:
        flask_process.terminate()
    icon.stop()

def main():
    icon = pystray.Icon(
        "AI Privacy Shield",
        create_icon(),
        "AI Privacy Shield",
        menu=pystray.Menu(
            pystray.MenuItem("🛡️ Protection: OFF", None, enabled=False),
            pystray.MenuItem("▶️ Start Protection", start_protection),
            pystray.MenuItem("❌ Exit", exit_app)
        )
    )
    icon.run()

if __name__ == '__main__':
    main()