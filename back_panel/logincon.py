import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, BASE_DIR)
from _modules import *
from options.userlog import checkuser
from userpanel.upanel import run
from options.users import add
from loading_page.main import run as loading_run
from adminpanel.apanel import run as admrun
TEXTS = "#5A1E2A"
FRAMES = "#F7F1E5"
TEXTSE = "#E7F2DF"
ENTRIE = "#839078"
PLACETEXTS = "#5A1E2A"
HOVER = "#6F7C63"
def afterl(window,userc):
    CTkMessagebox(
        message=f"Welcome {userc['name']}",
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
        sound="assests/sound/succes.mp3",
        )
    if userc["role"]=="Admin":
        admrun(window,userc)
    else:
        run(window,userc)
def afters(window,userc):
    CTkMessagebox(
        message=f"Welcome {userc['name']}",
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
        sound="assests/sound/succes.mp3",
    )
    run(window,userc)
def login(window,username, role, password):
    userc= checkuser(username, role, password)
    if userc:
        window.withdraw()
        loading_run(afterl ,window, userc)
        return userc
def signup(window,name,username,password):
    userc= add(name,username,password)
    if userc:
        userc= {
        "name":name,
        "username":username,
        "password":password,
        "role": "user"}
        window.withdraw()
        loading_run(afters, window, userc)