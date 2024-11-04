import tkinter as tk

def get_screen_resolution():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Adjust for title bar and borders (approximately)
    adjusted_width = screen_width - 10  # 5 pixels on each side
    adjusted_height = screen_height - 100  # 30 pixels for title bar

    return adjusted_width, adjusted_height