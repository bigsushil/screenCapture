# from PIL import ImageGrab
# import time
# import os
# from datetime import datetime

# def capture_screen(save_folder):
#     if not os.path.exists(save_folder):
#         os.makedirs(save_folder)

#     timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#     filepath = os.path.join(save_folder, f"screenshot_{timestamp}.png")
#     screenshot = ImageGrab.grab()
#     screenshot.save(filepath)
#     print(f"📸 Screenshot saved: {filepath}")

# def start_capture(interval_minutes=5, save_folder="C:\\ScreenCaptures"):
#     print(f"🕒 Starting screen capture every {interval_minutes} minutes...")
#     while True:
#         capture_screen(save_folder)
#         time.sleep(interval_minutes * 60)

# if __name__ == "__main__":
#     start_capture()
from PIL import ImageGrab
import time
import os
from datetime import datetime

def is_working_time():
    now = datetime.now()
    weekday = now.weekday()  # Monday = 0, Sunday = 6
    hour = now.hour
    return weekday < 5 and 9 <= hour < 18  # Mon–Fri, 9AM–6PM

def capture_screen(save_folder):
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filepath = os.path.join(save_folder, f"screenshot_{timestamp}.png")
    screenshot = ImageGrab.grab()
    screenshot.save(filepath)
    print(f"📸 Screenshot saved: {filepath}")

def start_capture(interval_minutes=5, save_folder="C:\\ScreenCaptures"):
    print("🕒 Monitoring weekdays during working hours...")
    while True:
        if is_working_time():
            capture_screen(save_folder)
        else:
            print("⏸️ Outside working hours. Skipping capture.")
        time.sleep(interval_minutes * 60)

if __name__ == "__main__":
    start_capture()
