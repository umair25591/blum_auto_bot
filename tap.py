# -*- coding: utf-8 -*-
from pyautogui import *
import pygetwindow as gw
import pyautogui
import time
import keyboard
import random
from pynput.mouse import Button, Controller
import tkinter as tk

mouse = Controller()
time.sleep(0.5)

print(f"YT:  https://www.youtube.com/@YoungBoy370")

window_input = "\nEnter window name (1 - TelegramDesktop): "
window_not_found = "[❌] | Window - {} not found!"
window_found = "[✅] | Window found - {}\nPress 'q' to pause."
pause_message = "Pause\nPress 'q' again to continue"
continue_message = "Continue working."

def click(x, y):
    mouse.position = (x, y)  # Move to the position
    time.sleep(0.1)  # Small delay to make sure the mouse is fully moved
    mouse.press(Button.left)  # Click left button
    mouse.release(Button.left)  # Release the button

window_name = input(window_input)

if window_name == '1':
    window_name = "TelegramDesktop"

if window_name == '2':
    window_name = "KotatogramDesktop"

check = gw.getWindowsWithTitle(window_name)
if not check:
    print(window_not_found.format(window_name))
else:
    print(window_found.format(window_name))

telegram_window = check[0]
paused = False

# Set the size of the central area to click (adjust as needed)
center_width = 380  # Width of the central area
center_height = 10  # Height of the central area

# Define the number of pixels you want to click per second (this part is modified for larger gap)
clicks_per_second = (center_width // 5) * (center_height // 2)  # Skipping 5 pixels in x and 2 pixels in y

print(f"Total clicks per second: {clicks_per_second}")

# Calculate the delay between clicks to fit within 1 second (adjust with a multiplier)
multiplier = 10  # Increase multiplier to slow down clicks
delay_between_clicks = (1 / clicks_per_second) * multiplier  # Adjusted delay

print(f"Delay between clicks: {delay_between_clicks}")


while True:
    if keyboard.is_pressed('q'):
        paused = not paused
        if paused:
            print(pause_message)
        else:
            print(continue_message)
        time.sleep(0.2)

    if paused:
        continue

    window_rect = (
        telegram_window.left, telegram_window.top, telegram_window.width, telegram_window.height
    )

    if telegram_window != []:
        try:
            telegram_window.activate()
        except:
            telegram_window.minimize()
            telegram_window.restore()

    # Calculate the top-left corner of the central area
    center_x = window_rect[0] + (window_rect[2] // 2) - (center_width // 2)
    center_y = window_rect[1] + (window_rect[3] // 2) - (center_height // 2)

    # Loop over the area and click every pixel
    for y in range(center_y, center_y + center_height):
        for x in range(center_x, center_x + center_width):
            click(x, y)  # Perform click at each position
            time.sleep(delay_between_clicks)  # Delay to ensure clicks happen within 1 second

    time.sleep(10)  # Small delay before repeating the loop
