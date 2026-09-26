import os
import json
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, BASE_DIR)
from _modules import *
from back_panel.card1 import *
TEXTS = "#5A1E2A"
FRAMES = "#F7F1E5"
ENTRIE = "#89977D"
PLACETEXTS = "#5A1E2A"
HOVER = "#6F7C63"
def addpack(pgk):
    if os.path.exists("data/packages.json"):
        with open("data/packages.json" ,"r") as file:
            p=json.load(file)
            p.append(pgk)
        with open("data/packages.json", "w") as file:
            json.dump(p,file)
    else:
        pc=[]
        pc.append(pgk)
        with open("data/packages.json","w") as file:
            json.dump(pc,file)
def deletepack(pgk):
    op=openj()
    for o in op:
        if o["tracking"]==pgk["tracking"]:
            op.remove(o)
            break
    with open("data/packages.json", "w") as file:
        json.dump(op,file)
def remove2(pgk):
    deletepack(pgk)
    CTkMessagebox(
            message="Deleted succesfully",
            icon="check",
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
    return True
    
