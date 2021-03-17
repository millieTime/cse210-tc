import os
from pathlib import Path
DIR = Path(__file__).resolve().parent
#This is the path we're looking for
DIRROOT = str(DIR.resolve().parent)
MAX_X = 800
MAX_Y = 500

BEAT_SPEED = 2
BEAT_Y = MAX_Y
# split the x-axis into 4 sections, start left to right
# 1st section
BEAT_X = {
    # 1st section
    "q" : (SCREEN_WIDTH / 4 * 1),
    # 2nd section
    "w" : (SCREEN_WIDTH / 4 * 2), 
    # 3rd section
    "e" : (SCREEN_WIDTH / 4 * 3), 
    # 4th section
    "r" : (SCREEN_WIDTH / 4 * 4), 
}

# a little higher than the bottom of the screen
DROP_POINT_Y = MAX_Y / 4
DROP_POINT_WIDTH = MAX_X

DROP_POINT_IMAGE = DIRROOT + "/assets/images/drop_point_activated.png"
DROP_POINT_IMAGE2 = DIRROOT + "/assets/images/drop_point_deactivated.png"
# BEAT_IMAGE
