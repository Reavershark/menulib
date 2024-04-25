import os
from menulib import *

#
# Config
#
menu = Menu(width=480, height=320)
os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"

buttons = [
    Button(text="test1", x=30, y=30,  width=210, height=55, font_color=RED, border_color=RED),
    Button(text="test2", x=30, y=105, width=210, height=55),
]

#
# Helper functions
#
def on_button_press(button: Button):
    print(f"Pressed button {button.text}!")

    if button.text == "test1":
        # Toggle color
        if button.font_color == RED:
            button.font_color = GREEN
            button.border_color = GREEN
        else:
            button.font_color = RED
            button.border_color = RED

#
# Callbacks
#
def setup():
    menu.screen.fill("purple")

def draw():
    menu.screen.fill("black")
    for button in buttons:
        menu.draw_button(button)

def on_touch(touch_x: int, touch_y: int):
    for button in buttons:
        if button.contains(touch_x, touch_y):
            on_button_press(button)

#
# Run
#
menu.run(setup=setup, draw=draw, on_touch=on_touch)
