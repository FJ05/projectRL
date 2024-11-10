import tkinter as tk
# A function to get the screen resolution of the screen/computer the game is being run on.
def get_screen_resolution():
    # This code is taken from forum https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python
    # And was found to be an easy solution due to tkinter being part of python.
    root = tk.Tk()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Adjust for title bar and borders (approximately)
    adjusted_width = screen_width - 10  # 5 pixels on each side
    adjusted_height = screen_height - 100  # 30 pixels for title bar
    # returns the screen size
    return adjusted_width, adjusted_height