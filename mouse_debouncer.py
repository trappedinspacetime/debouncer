#!/usr/bin/env python3
from pynput.mouse import Listener
import time
# Debounce interval in seconds
DEBOUNCE_INTERVAL = 0.2

# Global variables to track mouse clicks
last_click_time = 0
last_click_button = None

def on_click(x, y, button, pressed):
    global last_click_time, last_click_button

    # Check if it's a new click and not a release event
    if pressed and button != last_click_button:
        current_time = time.time()
        if current_time - last_click_time > DEBOUNCE_INTERVAL:
            # Perform your desired action here
            print(f"Clicked {button} at ({x}, {y})")

        last_click_time = current_time
        last_click_button = button

# Start listening for mouse events
with Listener(on_click=on_click) as listener:
    listener.join()

