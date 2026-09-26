import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, BASE_DIR)
from _modules import *
from options.back import *
from options.userlog import checkuser
from back_panel.logincon import login

TEXTS = "#5A1E2A"
FRAMES = "#F7F1E5"
TEXTSE = "#E7F2DF"
ENTRIE = "#839078"
PLACETEXTS = "#5A1E2A"
HOVER = "#6F7C63"
role = ["User", "Admin"]


def componentsfr1(fr1, switchsignin, window):
    password = StringVar(value="*")
    user = StringVar()
    pas = StringVar()
    lbl1 = CTkLabel(
        fr1, text="Welcome back", text_color=TEXTS, font=("Nova Bomb SemBd", 35)
    )
    lbl1.place(y=50, relx=0.5, anchor="center")
    lbl2 = CTkLabel(
        fr1, text="Join the RESPAWNIX", text_color=TEXTS, font=("Nova Bomb SemBd", 20)
    )
    lbl2.place(y=110, relx=0.5, anchor="center")
    lbl3 = CTkLabel(
        fr1, text="Username", text_color=TEXTS, font=("Nova Bomb SemBd", 20)
    )
    lbl3.place(y=170, relx=0.2)
    entry1 = CTkEntry(
        fr1,
        placeholder_text="Enter your username",
        text_color=TEXTSE,
        placeholder_text_color=PLACETEXTS,
        corner_radius=16,
        fg_color=ENTRIE,
        width=250,
        height=40,
        font=("GROSTE", 20),
        textvariable=user,border_width=0
    )
    entry1.place(y=230, relx=0.5, anchor="center")
    lbl4 = CTkLabel(fr1, text="Role", text_color=TEXTS, font=("Nova Bomb SemBd", 20))
    lbl4.place(y=300, relx=0.2)
    combo = CTkComboBox(
        fr1,
        values=role,
        fg_color=ENTRIE,
        text_color=TEXTSE,
        font=("GROSTE", 15),
        dropdown_fg_color=ENTRIE,
        dropdown_text_color=FRAMES,
        width=200,
        height=40,
        button_color=ENTRIE,
        dropdown_font=("GROSTE", 15),
        button_hover_color=HOVER,
        dropdown_hover_color=HOVER,
        corner_radius=16,
        justify="center",border_width=0
    )
    combo.set("Who are you?")
    combo.place(relx=0.3, y=300)
    lbl5 = CTkLabel(
        fr1, text="Password", text_color=TEXTS, font=("Nova Bomb SemBd", 20)
    )
    lbl5.place(y=380, relx=0.2)
    entry3 = CTkEntry(
        fr1,
        placeholder_text="Enter your password",
        text_color=TEXTSE,
        placeholder_text_color=PLACETEXTS,
        corner_radius=16,
        fg_color=ENTRIE,
        width=250,
        height=40,
        font=("Arial", 20),
        show="*",
        textvariable=pas,border_width=0
    )
    entry3.place(y=440, relx=0.5, anchor="center")
    btneye = load_photo(
        "assests/images/eye.png",
        fr1,
        (30, 30),
        FRAMES,
        widget="button",
        hover=HOVER,
        widthb=30,
        heightb=30,
        commnd=lambda: spassword(entry3, password),
    )
    btneye.place(y=420, relx=0.79)
    btn2 = CTkButton(
        fr1,
        text="Confirm",
        fg_color=TEXTS,
        text_color=FRAMES,
        hover_color=HOVER,
        corner_radius=13,
        height=40,
        font=("Nova Bomb SemBd", 20),
        cursor="hand2",
        command=lambda: login(window, user.get(), combo.get(), pas.get()),
    )
    btn2.place(relx=0.5, anchor="center", y=560)
    btn3 = CTkButton(
        fr1,
        text="Dont have an account? sign in.",
        text_color=TEXTS,
        hover_color=HOVER,
        corner_radius=13,
        height=40,
        font=("Nova Bomb SemBd", 15),
        cursor="hand2",
        fg_color=FRAMES,
        command=lambda: switchsignin(fr1, window),
    )
    btn3.place(relx=0.2, y=460)
