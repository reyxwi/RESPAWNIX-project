import json
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, BASE_DIR)
from _modules import *
from back_panel.card1 import *
from userpanel.panel_options.deletepack import *
TEXTS = "#5A1E2A"
FRAMES = "#F7F1E5"
ENTRIE = "#89977D"
PLACETEXTS = "#5A1E2A"
HOVER = "#6F7C63"
def openj():
    with open("data/packages.json","r") as file:
        pack=json.load(file)
        return pack
def readj(pack,userc):
    packs=[]
    for p in pack:
        if p["username"]==userc["username"]:
            packs.append(p)
    return packs
def find(track,userc):
    open=openj()
    for o in open:
        if o["tracking"]==track and o["username"]==userc["username"]:
            return o
    CTkMessagebox(
            message="Nothing",
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
def un(pack,userc):
    packs=[]
    for p in pack:
        if p["username"]==userc["username"]:
            if p["status"]=="unknown":
                packs.append(p)
    return packs