import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, BASE_DIR)
from _modules import *
from options.back import *
from userpanel.upanel import run
from back_panel.logincon import signup

TEXTS = "#5A1E2A"
FRAMES = "#F7F1E5"
TEXTSE = "#E7F2DF"
ENTRIE = "#839078"
PLACETEXTS = "#5A1E2A"
HOVER = "#6F7C63"


def setwindow():
    window = CTk()
    window.geometry("1000x650")
    window.resizable(False, False)
    window.configure(fg_color=TEXTS)
    window.title("sign up")
    return window


def frames(window):
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    fr1 = CTkFrame(
        window,
        width=400,
        height=600,
        fg_color=FRAMES,
        corner_radius=20,
        border_color="black",
    )
    fr1.grid(row=0, column=1, padx=50, pady=30, sticky="nsew")
    fr2 = CTkFrame(
        window,
        width=300,
        height=600,
        fg_color=FRAMES,
        corner_radius=20,
        border_color="black",
    )
    fr2.grid(row=0, column=0, padx=50, pady=30, sticky="nsew")
    return fr1, fr2


def componentsfr1s(fr1, switchlogin, window):
    password = StringVar(value="*")
    n = StringVar()
    user = StringVar()
    pas = StringVar()
    lbl1 = CTkLabel(
        fr1, text="Create your account", text_color=TEXTS, font=("Nova Bomb SemBd", 35)
    )
    lbl1.place(y=50, relx=0.5, anchor="center")
    lbl2 = CTkLabel(
        fr1, text="Join the RESPAWNIX", text_color=TEXTS, font=("Nova Bomb SemBd", 20)
    )
    lbl2.place(y=110, relx=0.5, anchor="center")
    lbl3 = CTkLabel(fr1, text="Name", text_color=TEXTS, font=("Nova Bomb SemBd", 20))
    lbl3.place(y=170, relx=0.2)
    entry1 = CTkEntry(
        fr1,
        placeholder_text="Enter your Name",
        text_color=TEXTSE,
        placeholder_text_color=PLACETEXTS,
        corner_radius=16,
        fg_color=ENTRIE,
        width=250,
        height=40,
        font=("GROSTE", 20),
        textvariable=n,
        border_width=0,
    )
    entry1.place(y=230, relx=0.5, anchor="center")
    lbl4 = CTkLabel(
        fr1, text="Username", text_color=TEXTS, font=("Nova Bomb SemBd", 20)
    )
    lbl4.place(y=280, relx=0.2)
    entry2 = CTkEntry(
        fr1,
        placeholder_text="Enter your username",
        text_color=TEXTSE,
        placeholder_text_color=PLACETEXTS,
        corner_radius=16,
        fg_color=ENTRIE,
        width=250,
        height=40,
        font=("GROSTE", 20),
        textvariable=user,
        border_width=0,
    )
    entry2.place(y=340, relx=0.5, anchor="center")
    lbl5 = CTkLabel(
        fr1, text="Password", text_color=TEXTS, font=("Nova Bomb SemBd", 20)
    )
    lbl5.place(y=390, relx=0.2)
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
        textvariable=pas,
        border_width=0,
    )
    entry3.place(y=450, relx=0.5, anchor="center")
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
    btneye.place(y=435, relx=0.79)
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
        command=lambda: signup(window, n.get(), user.get(), pas.get()),
    )
    btn2.place(relx=0.5, anchor="center", y=560)
    btn3 = CTkButton(
        fr1,
        text="Already have an account? log in.",
        text_color=TEXTS,
        hover_color=HOVER,
        corner_radius=13,
        height=40,
        font=("Nova Bomb SemBd", 15),
        cursor="hand2",
        fg_color=FRAMES,
        command=lambda: switchlogin(fr1, window),
    )
    btn3.place(relx=0.2, y=475)


def componentsfr2(fr2):
    lbl1 = CTkLabel(
        fr2, text="RESPAWNIX", text_color=TEXTS, font=("Pixel O10 Bott", 35)
    )
    lbl1.place(y=50, relx=0.5, anchor="center")
    tracklbl = load_photo(
        "assests/images/tracking.png", fr2, (300, 200), FRAMES, widget="label"
    )
    tracklbl.place(relx=0.5, anchor="center", y=200)
    lbl1 = CTkLabel(
        fr2,
        text="Track it.\n\nManage it.\n\nDeliver it.",
        text_color=TEXTS,
        font=("Nova Bomb SemBd", 25),
    )
    lbl1.place(y=350, relx=0.5, anchor="center")
    lbl2 = CTkLabel(
        fr2, text="──────────────────────────", text_color=TEXTS, font=("Arial", 15)
    )
    lbl2.place(y=450, relx=0.5, anchor="center")
    lbl3 = CTkLabel(
        fr2,
        text="Enter the Game, \nIgnite the Flame.",
        text_color=TEXTS,
        font=("Pixel O10 Bott", 25),
    )
    lbl3.place(y=500, relx=0.5, anchor="center")


# def run():

#     window=setwindow()
#     fr1,fr2=frames(window)
#     comf1=componentsfr1s(fr1)
#     comfr2=componentsfr2(fr2)
#     window.mainloop()

# if __name__ == "__main__":
#     run()
