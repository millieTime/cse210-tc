import arcade
from game import constants

class Countdown(arcade.Sprite):
    # want this to show 3, 2, 1, so I'll need to override update and increment some timer to keep track of the number here.
    # Won't have pictures so much as it will have text that starts big nd gets small.