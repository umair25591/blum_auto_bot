import pyautogui
import pygetwindow as gw
import time
import keyboard
import threading

window_input = "\nEnter window name (1 - TelegramDesktop): "
window_not_found = "[❌] | Window - {} not found!"
window_found = "[✅] | Window found - {}\nPress 'q' to pause."
pause_message = "Pause\nPress 'q' again to continue"
continue_message = "Continue working."

def click(x, y):
    pyautogui.click(x, y)  # Perform the click at the given coordinates without moving the mouse

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

# Define the number of pixels you want to click per second
clicks_per_second = (center_width // 5) * (center_height // 2)

print(f"Total clicks per second: {clicks_per_second}")

def perform_clicks():
    window_rect = (
        telegram_window.left, telegram_window.top, telegram_window.width, telegram_window.height
    )

    # Calculate the top-left corner of the central area
    center_x = window_rect[0] + (window_rect[2] // 2) - (center_width // 2)
    center_y = window_rect[1] + (window_rect[3] // 2) - (center_height // 2)

    # Create a list to store the threads for each click position
    threads = []

    # Loop over the area and perform the clicks using threads
    for y in range(center_y, center_y + center_height, 2):  # Adjust the step size (y-axis gap)
        for x in range(center_x, center_x + center_width, 5):  # Adjust the step size (x-axis gap)
            # Start a new thread for each click position
            thread = threading.Thread(target=click, args=(x, y))
            threads.append(thread)
            thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

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

    # Ensure window is activated
    if telegram_window != []:
        try:
            telegram_window.activate()
        except:
            telegram_window.minimize()
            telegram_window.restore()

    # Perform all clicks at once (in parallel)
    perform_clicks()

    print("All clicks performed at once.")
    time.sleep(0.2)  # Wait for 1 second before performing the next batch of clicks
