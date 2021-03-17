import os
from pathlib import Path
DIR = Path(__file__).resolve().parent
#This is the path we're looking for
DIRROOT = str(DIR.resolve().parent)
MAX_X = 900
MAX_Y = 700

BEAT_SPEED = -200
BEAT_SCALE = .75
BEAT_Y = MAX_Y
# split the x-axis into 4 sections, start left to right
# 1st section
BEAT_X = {
    # 1st section
    "q" : (MAX_X / 4 * 0.5),
    # 2nd section
    "w" : (MAX_X / 4 * 1.5),
    # 3rd section
    "e" : (MAX_X / 4 * 2.5),
    # 4th section
    "r" : (MAX_X / 4 * 3.5)
}
BEAT_IMAGES = {
    "q" : DIRROOT + "/assets/images/beat_q.png",
    "w" : DIRROOT + "/assets/images/beat_w.png",
    "e" : DIRROOT + "/assets/images/beat_e.png",
    "r" : DIRROOT + "/assets/images/beat_r.png"
}
# a little higher than the bottom of the screen
DROP_POINT_Y = MAX_Y / 4
DROP_POINT_WIDTH = MAX_X
DROP_POINT_IMAGE = DIRROOT+"/assets/images/beat_blank_trans.png"
DROP_POINT_IMAGE_2 = DIRROOT+"/assets/images/beat_blank_active.png"



