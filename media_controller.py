import os
import guli
import keyboard
def playpause():
    keyboard.press_and_release("k")
def mute():
    keyboard.press_and_release("m")
def skip():
    keyboard.press_and_release("shift+n")
def prev():
    keyboard.press_and_release("shift+p")
def increase_volume():
    keyboard.press_and_release("up")
def decrease_volume():
    keyboard.press_and_release("down")