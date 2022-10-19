import turtle

# Create Window
wn = turtle.Screen()
wn.title("Radar")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Heading
# TODO: hdg should come in as an input
hdg = f'{24:03d}'
degree_sign = u'\N{DEGREE SIGN}'

# Hide turtle and set start location/color
turtle.ht()
turtle.color("lime")
turtle.penup()
turtle.goto(0,215)

# Display Heading indicator
turtle.write(f"{hdg}{degree_sign}", False, align='center', font=('Futura Medium', 12, 'normal'))

# Main Loop
while True:
    # update screen
    wn.update()
