import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, BASE_DIR)
from _modules import *

TEXTS = "#5A1E2A"
FRAMES = "#F7F1E5"
ENTRIE = "#89977D"
PLACETEXTS = "#5A1E2A"
HOVER = "#6F7C63"


def emptyadd(name, dest, tran):
    if name == "" or dest == "" or tran == "":
        CTkMessagebox(
            message="fill all the fields.",
            icon="cancel",
            options="Ok.",
            fg_color=FRAMES,
            text_color=TEXTS,
            button_hover_color=HOVER,
            button_text_color=TEXTS,
            title="Erorr",
            title_color=FRAMES,
            button_color=FRAMES,
            corner_radius=16,
            font=("Nova Bomb SemBd", 20),
            sound="assests/sound/error.mp3",
        )
        return False
