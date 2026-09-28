import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, BASE_DIR)
from _modules import *
from validation.empty import *
TEXTS = "#5A1E2A"
FRAMES = "#F7F1E5"
ENTRIE = "#89977D"
PLACETEXTS = "#5A1E2A"
HOVER = "#6F7C63"

def checksign(name, username, password, users):
    res = emptyen(name, username, password)
    if res == False:
        return False
    for u in users:
        if username == u["username"] and password == u["password"]:
            CTkMessagebox(
                message="password and username in already in use.",
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
        elif username == u["username"]:
            CTkMessagebox(
                message="username is already in use.",
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
        elif password == u["password"]:
            CTkMessagebox(
                message="password in already in use.",
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

    # CTkMessagebox(
    #     message=f"Welcome {name}",
    #     icon="check",
    #     options="Ok.",
    #     fg_color=FRAMES,
    #     text_color=TEXTS,
    #     button_hover_color=HOVER,
    #     button_text_color=TEXTS,
    #     title="Erorr",
    #     title_color=FRAMES,
    #     button_color=FRAMES,
    #     corner_radius=16,
    #     font=("Nova Bomb SemBd", 20),
    #     sound="assests/sound/succes.mp3",
    # )
    return True
