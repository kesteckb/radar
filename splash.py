from tkinter import *
from PIL import ImageTk, Image
import time

class Splash:
    def __init__(self, app_width, app_height):
        self.app_width = app_width
        self.app_height = app_height

    def splash_start(self):  
        splash_root = Tk()

        # Find Screen Dimensions
        screen_width = splash_root.winfo_screenwidth()
        screen_height = splash_root.winfo_screenheight()

        # Find coordinates for top left corner of app to be centered in screen
        window_x = int((screen_width / 2) - (self.app_width / 2))
        window_y = int((screen_height / 2) - (self.app_height / 2))

        # Window name and size
        splash_root.title("Splash Screen")
        splash_root.geometry(f'{self.app_width}x{self.app_height}+{window_x}+{window_y}')

        # Set up canvas
        splash_screen = Canvas(splash_root)
        splash_screen.pack(fill="both", expand=True)

        # Define image
        my_img = ImageTk.PhotoImage(Image.open('images/f_14_sunrise.png'))

        # Set image in canvas
        splash_screen.create_image(0, 0, image=my_img, anchor="nw")

        # Hide Title Bar
        splash_root.overrideredirect(True)

        # Display Image
        
        my_label = Label(image=my_img)
        my_label.pack()

        time.sleep(.001)
        splash_root.destroy()