import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, BASE_DIR)
from _modules import *
from back_panel.card1 import *
from panel_options.deletepack import *
TEXTS = "#5A1E2A"
FRAMES = "#F7F1E5"
ENTRIE = "#89977D"
PLACETEXTS = "#5A1E2A"
HOVER = "#6F7C63"
def remove(userc,te):
    if te.get() == "":
        CTkMessagebox(
            message="Fill the field.",
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
    pgk=find(te.get(),userc)
    rund(pgk)
    return True
   