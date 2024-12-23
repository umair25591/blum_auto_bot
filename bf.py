# -*- coding: utf-8 -*-
from pyautogui import *
import pygetwindow as gw
import pyautogui
import time
import keyboard
import random
from pynput.mouse import Button, Controller
from PIL import Image, ImageEnhance, ImageFilter 
import pytesseract

mouse = Controller()
time.sleep(0.5)

print(f"YT:  https://www.youtube.com/@YoungBoy370")

window_input = "\nEnter window name (1 - TelegramDesktop): "
window_not_found = "[❌] | Window - {} not found!"
window_found = "[✅] | Window found - {}\nPress 'q' to pause."
pause_message = "Pause\nPress 'q' again to continue"
continue_message = "Continue working."

def click(x, y):
    mouse.position = (x, y + random.randint(1, 3))
    mouse.press(Button.left)
    mouse.release(Button.left)

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

    scrn = pyautogui.screenshot(region=(window_rect[0], window_rect[1], window_rect[2], window_rect[3]))

    width, height = scrn.size
    pixel_found = False

    if pixel_found == True:
        break

    for x in range(0, width, 20):
        for y in range(0, height, 20):
            r, g, b = scrn.getpixel((x, y))

            # Check for white pixels or the specific color (132, 56, 7)
            # if (r in range(240, 256)) and (g in range(240, 256)) and (b in range(240, 256)):
            #     # This is for detecting white pixels
            #     screen_x = window_rect[0] + x
            #     screen_y = window_rect[1] + y
            #     click(screen_x + 4, screen_y)
            #     time.sleep(0.001)
            #     pixel_found = True
            #     break
            # elif (r == 132) and (g == 56) and (b == 7):
            #     # This is for detecting the specific color (132, 56, 7)
            #     screen_x = window_rect[0] + x
            #     screen_y = window_rect[1] + y
            #     click(screen_x + 4, screen_y)
            #     time.sleep(0.001)
            #     pixel_found = True
            #     break
            # elif (r in range(245, 256)) and (g in range(10, 50)) and (b in range(180, 200)):
            #     # This is for detecting shades of pink (R: 255, G: 14, B: 192)
            #     screen_x = window_rect[0] + x
            #     screen_y = window_rect[1] + y
            #     click(screen_x + 4, screen_y)
            #     time.sleep(0.001)
            #     pixel_found = True
            #     break


            if (r in range(240, 256)) and (g in range(240, 256)) and (b in range(240, 256)):
                # This is for detecting white pixels
                screen_x = window_rect[0] + x
                screen_y = window_rect[1] + y
                click(screen_x + 4, screen_y)
                time.sleep(0.001)
                pixel_found = True
                break
            elif (r in range(120, 150)) and (g in range(50, 70)) and (b in range(0, 40)):
                # This is for detecting shades of brown near (132, 56, 7)
                screen_x = window_rect[0] + x
                screen_y = window_rect[1] + y
                click(screen_x + 4, screen_y)
                time.sleep(0.001)
                pixel_found = True
                break
            elif (r in range(180, 255)) and (g in range(70, 150)) and (b in range(70, 150)):
                # This is for detecting shades of pink
                screen_x = window_rect[0] + x
                screen_y = window_rect[1] + y
                click(screen_x + 4, screen_y)
                time.sleep(0.001)
                pixel_found = True
                break
            elif (r in range(250, 256)) and (g in range(150, 170)) and (b in range(0, 50)):
                # This is for detecting shades of orange
                screen_x = window_rect[0] + x
                screen_y = window_rect[1] + y
                click(screen_x + 4, screen_y)
                time.sleep(0.001)
                pixel_found = True
                break
            elif (r in range(90, 110)) and (g in range(160, 180)) and (b in range(20, 60)):
                # This is for detecting shades of green near (100, 169, 39)
                screen_x = window_rect[0] + x
                screen_y = window_rect[1] + y
                click(screen_x + 4, screen_y)
                time.sleep(0.001)
                pixel_found = True
                break



                # if pixel_found:
                #     break

    # Only if the color pattern was not found, check for the "Play" text
    
    if not pixel_found:


        d = pytesseract.image_to_data(scrn, output_type=pytesseract.Output.DICT)

        print(d['text'])

        for i in range(len(d['text'])):
            if "Play" in d['text'][i] or "left" in d['text'][i]:
                x = d['left'][i] + window_rect[0]
                y = d['top'][i] + window_rect[1]
                w = d['width'][i]
                h = d['height'][i]
                click(x + w // 2, y + h // 2)  # Click the center of the detected text
                break
