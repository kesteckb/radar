
from cProfile import run
import random
import turtle
import time
from tkinter import *
from PIL import ImageTk, Image
from sweep import sweep
from inbounds import *
import bandit

# Create Window
root = Tk()
root.title("Radar")
root.iconbitmap("images/radar_icon_16.ico")

# Designate app Height and Width
app_width = 800
app_height = 480

# Find Screen Dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Find coordinates for top left corner of app to be centered in screen
window_x = int((screen_width / 2) - (app_width / 2))
window_y = int((screen_height / 2) - (app_height / 2))

# Set window size and position
root.geometry(f'{app_width}x{app_height}+{window_x}+{window_y}')

# Define Image
bg = ImageTk.PhotoImage(file="images/background_1.png")

# Set up canvas
my_canvas = Canvas(root)
my_canvas.pack(fill="both", expand=True)

# Set background image in canvas
my_canvas.create_image(0,0, image=bg, anchor="nw")

# Function to close program by clicking close window button
def handler():
    global run
    run = False

# Set run to False when close button clicked
root.protocol("WM_DELETE_WINDOW", handler)

# run set to True by default
run = True

# Main Loop
bogeys = []
hdg = random.randrange(0, 360)
degree_sign = u'\N{DEGREE SIGN}'

while run:
    root.update()

    # Delete bogeys from previous frame
    my_canvas.delete("bogey")
    
    # Find bandits
    bogeys = sweep(bogeys)

    # Handle bogeys
    if bogeys is not None or len(bogeys) > 0:
        for bogey in bogeys:
            bandit_x, bandit_y = bogey.get_position()
            direct_x, direct_y = bogey.get_direction()

            # Create Bogey Symbol
            my_canvas.create_rectangle(
                    bandit_x-10, 
                    bandit_y-10, 
                    bandit_x+10, 
                    bandit_y+10,
                    outline = "lime", 
                    fill=None,
                    tag="bogey",
                    width=3,
                )

            my_canvas.create_oval(
                    bandit_x - 3,
                    bandit_y - 3,
                    bandit_x + 3,
                    bandit_y + 3,
                    outline = "lime",
                    fill = "lime",
                    width = 3,
                    tag = "bogey",            
                )
        
            my_canvas.create_line(
                    bandit_x, 
                    bandit_y, 
                    direct_x, 
                    direct_y, 
                    fill="lime", 
                    width=3, 
                    tag="bogey",
                )

    # Get Heading
    # TODO: handle as input from sensor
    hdg += random.randrange(-3, 3)
    if hdg < 0:
        hdg = 360 + hdg
    elif hdg > 359:
        hdg = hdg - 360
    my_canvas.create_text(
            402, 
            48, 
            text=f"{hdg:03d}{degree_sign}", 
            fill="lime", 
            font=("Futura", 12), 
            tag="bogey"
        )

    # Delay screen refresh
    time.sleep(.5)
    
# Destroy Window
root.destroy()