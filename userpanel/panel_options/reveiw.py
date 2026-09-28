import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, BASE_DIR)
from _modules import *
from options.back import load_photo
TEXTST="#353535"
FRAMEST="#DFDDD7" 
ENTRIE = "#E9F9DB"
HOVER="#6F7C63"


def repack():
    top = CTkToplevel()
    top.geometry("400x500")
    top.title("your package review")
    top.configure(fg_color=TEXTST)
    top.resizable(False, False)
    top.attributes("-topmost", True)
    top.overrideredirect(True)
    return top


def repackcon(top, pgk):
    tr = pgk["tracking"]
    r = pgk["reciever"]
    d = pgk["destenation"]
    s = pgk["status"]
    lbl = CTkLabel(
        top,
        text="Here is your package reveiw",
        text_color=FRAMEST,
        font=("Nova Bomb SemBd", 20),
    )
    lbl.place(relx=0.5, anchor="center", y=30)
    fr = CTkFrame(top, width=300, height=400, fg_color=FRAMEST, corner_radius=16)
    fr.place(relx=0.5, anchor="center", rely=0.55)
    box = load_photo("assests/images/box.png", fr, (100, 100), widget="label")
    box.place(relx=0.5, anchor="center", rely=0.13)
    lbl1 = CTkLabel(
        fr,
        text=f" your tracking ID: {tr}",
        text_color=TEXTST,
        font=("Nova Bomb SemBd", 20),
    )
    lbl1.place(relx=0.5, anchor="center", rely=0.28)
    lbl2 = CTkLabel(
        fr,
        text="────────────",
        text_color=TEXTST,
        font=("Nova Bomb SemBd", 20),
        fg_color=FRAMEST,
    )
    lbl2.place(relx=0.5, anchor="center", rely=0.4)
    lbl3 = CTkLabel(
        fr,
        text=f"Reciever :      {r}    ",
        text_color=TEXTST,
        font=("Nova Bomb SemBd", 20),
        border_width=0,
    )
    lbl3.place(relx=0.5, anchor="center", rely=0.5)
    lbl4 = CTkLabel(
        fr,
        text=f"Destenation :      {d}  ",
        text_color=TEXTST,
        font=("Nova Bomb SemBd", 20),
        border_width=0,
    )
    lbl4.place(relx=0.5, anchor="center", rely=0.6)
    lbl5 = CTkLabel(
        fr,
        text=f"Status :      {s}   ",
        text_color=TEXTST,
        font=("Nova Bomb SemBd", 20),
        border_width=0,
    )
    lbl5.place(relx=0.5, anchor="center", rely=0.7)
    btn2 = CTkButton(
        fr,
        text="Got it.",
        fg_color=TEXTST,
        text_color=FRAMEST,
        hover_color=HOVER,
        corner_radius=13,
        height=40,
        font=("Nova Bomb SemBd", 20),
        cursor="hand2",
        command=lambda: destroy(top),
    )
    btn2.place(relx=0.5, anchor="center", rely=0.8)


def runt(pgk):
    top = repack()
    repackcon(top, pgk)
    top.mainloop()


def destroy(top: CTkToplevel):
    top = top.winfo_toplevel()
    top.destroy()
