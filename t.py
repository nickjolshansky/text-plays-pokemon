import pyautogui

# Get a list of all the open windows
all_windows = pyautogui.getWindowsWithTitle('')

# Print the title of each window
for window in all_windows:
    print(window.title)