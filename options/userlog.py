import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, BASE_DIR)
from _modules import *
from validation.validation import *
from validation.empty import *

TEXTS = "#5A1E2A"
FRAMES = "#F7F1E5"
ENTRIE = "#89977D"
PLACETEXTS = "#5A1E2A"
HOVER = "#6F7C63"


def checkuser(username, role, password):
    with open("data/role.json", "r") as file:
        users = json.load(file)
        res = check(username, role, password)
        if res == False:
            return False
    for u in users:
        if password == u["password"] and username == u["username"]:
            name = u["name"]
            if role.lower() == "admin":
                if u["role"] == "Admin":
                    CTkMessagebox(
                        message=f"Welcome back {name} ",
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
                    return u
                else:
                    CTkMessagebox(
                        message="You are not an admin.",
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
            #         return False
            # CTkMessagebox(
            #     message=f"Welcome back {name} ",
            #     icon="check",
            #     options="Ok.",
            #     fg_color=FRAMES,
            #     text_color=TEXTS,
            #     button_hover_color=HOVER,
            #     button_text_color=TEXTS,
            #     title="Success",
            #     title_color=FRAMES,
            #     button_color=FRAMES,
            #     corner_radius=16,
            #     font=("Nova Bomb SemBd", 20),
            #     sound="assests/sound/succes.mp3",
            # )
            return u
    CTkMessagebox(
        message="Access Denied!",
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


def check(username, role, password):
    res = emptyen(username, role, password)
    if res == False:
        return False
