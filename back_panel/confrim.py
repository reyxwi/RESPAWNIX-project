import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, BASE_DIR)
from _modules import *
from options.pack import addpgk
from options.jpack import addpack
from userpanel.panel_options.reveiw import *

TEXTS = "#5A1E2A"
FRAMES = "#F7F1E5"
ENTRIE = "#89977D"
PLACETEXTS = "#5A1E2A"
HOVER = "#6F7C63"


def confrim(userc, rvar, dvar, svar):
    if rvar.get() == "" or dvar.get() == "" or svar.get() == "":
        CTkMessagebox(
            message="Fill all the fields.",
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
    pgk = addpgk(userc, rvar.get(), dvar.get(), svar.get())
    addpack(pgk)
    CTkMessagebox(
        message=f"Succesfully added",
        icon="check",
        options="Ok.",
        fg_color=FRAMES,
        text_color=TEXTS,
        button_hover_color=HOVER,
        button_text_color=TEXTS,
        title="Success",
        title_color=FRAMES,
        button_color=FRAMES,
        corner_radius=16,
        font=("Nova Bomb SemBd", 20),
        sound="assests/sound/succes.mp3",
    )
    runt(pgk)
