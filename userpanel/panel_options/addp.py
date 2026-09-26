import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, BASE_DIR)
from _modules import *
from options.back import *
from options.pack import *
from back_panel.confrim import confrim

FRAMES = "#5A1E2A"
TEXTS = "#F7F1E5"
TEXTSE = "#646B5F"
ENTRIE = "#E9F9DB"
PLACETEXTS = "#5A1E2A"
HOVER = "#6F7C63"


def cleanfr2pw(fr2pw, userc):
    for f in fr2pw.winfo_children():
        f.destroy()
    addpa(
        fr2pw,
        userc,
    )


def addpa(fr2pw, userc):
    svar = StringVar()
    rvar = StringVar()
    dvar = StringVar()
    tranval = ["Tipaks", "Pishtaz", "Alo Pake"]
    lbl1 = CTkLabel(
        fr2pw,
        text="What do you wanna order?",
        text_color=FRAMES,
        font=("Nova Bomb SemBd", 35),
    )
    lbl1.place(y=50, relx=0.5, anchor="center")
    lbl2 = CTkLabel(
        fr2pw,
        text="Add your package RESPAWNIX",
        text_color=FRAMES,
        font=("Nova Bomb SemBd", 20),
    )
    lbl2.place(y=110, relx=0.5, anchor="center")
    fr = CTkFrame(fr2pw, fg_color=FRAMES, corner_radius=16, width=430, height=450)
    fr.place(relx=0.5, anchor="center", rely=0.6)
    lbl3 = CTkLabel(fr, text="Reciever", text_color=TEXTS, font=("Nova Bomb SemBd", 20))
    lbl3.place(y=20, relx=0.2)
    entry1 = CTkEntry(
        fr,
        placeholder_text="Enter your Name",
        text_color=TEXTSE,
        placeholder_text_color=PLACETEXTS,
        corner_radius=16,
        fg_color=ENTRIE,
        width=250,
        height=40,
        font=("GROSTE", 20),
        textvariable=rvar,
    )
    entry1.place(y=80, relx=0.5, anchor="center")
    lbl4 = CTkLabel(
        fr, text="Destenation", text_color=TEXTS, font=("Nova Bomb SemBd", 20)
    )
    lbl4.place(y=150, relx=0.2)
    entry2 = CTkEntry(
        fr,
        placeholder_text="Enter your destenation",
        text_color=TEXTSE,
        placeholder_text_color=PLACETEXTS,
        corner_radius=16,
        fg_color=ENTRIE,
        width=250,
        height=40,
        font=("GROSTE", 20),
        textvariable=dvar,
    )
    entry2.place(y=210, relx=0.5, anchor="center")
    # ra=CTkRadioButton(fr,text="Small",fg_color=ENTRIE,hover_color=HOVER,text_color=TEXTS,variable=svar,value="Small",font=("GROSTE",20))
    # ra.pack(padx=40,pady=300,side="left")
    # ra2=CTkRadioButton(fr,text="Meduim",fg_color=ENTRIE,hover_color=HOVER,text_color=TEXTS,variable=svar,value="Meduim",font=("GROSTE",20))
    # ra2.pack(padx=40,pady=300,side="left")
    # ra3=CTkRadioButton(fr,text="Large",fg_color=ENTRIE,hover_color=HOVER,text_color=TEXTS,variable=svar,value="Large",font=("GROSTE",20))
    # ra3.pack(padx=40,pady=300,side="left")
    combo = CTkComboBox(
        fr,
        values=tranval,
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
        justify="center",
        variable=svar,
    )
    combo.set("choose your transpost")
    combo.place(relx=0.5, anchor="center", y=300)
    btn1 = CTkButton(
        fr,
        text="Confirm",
        fg_color=TEXTS,
        text_color=FRAMES,
        hover_color=HOVER,
        corner_radius=13,
        height=40,
        font=("Nova Bomb SemBd", 20),
        cursor="hand2",
        command=lambda: confrim(userc, rvar, dvar, svar),
    )
    btn1.place(relx=0.5, anchor="center", y=380)
