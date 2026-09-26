import os
import sys
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0,BASE_DIR)
from _modules import *
from options.back import *
from back_panel.card1 import *
from userpanel.panel_options.deletere import *
TEXTS="#5A1E2A"
FRAMES="#F7F1E5"
ENTRIE = "#E9F9DB"
PLACETEXTS="#5A1E2A"
TEXTSE = "#646B5F"
HOVER="#6F7C63"
te=None
def set(track):
    te.set(track)
def search(event,userc,frre,):
    text=te.get()
    if text!="":
        frre.place(relx=0.5,anchor="center",y=190)
    for f in frre.winfo_children():
        f.destroy()
    op=openj()
    re=readj(op, userc)
    for r in re:
        if text in r["tracking"]:
           btnre=CTkButton(frre,text=r["tracking"],text_color=TEXTS,font=("GROSTE", 20),hover_color=HOVER,corner_radius=13,cursor="hand2",fg_color=FRAMES,command=lambda tracking=r["tracking"]: set(tracking))
           btnre.pack()
def cleanfde(fr2pw,userc):
    for f in fr2pw.winfo_children():
        f.destroy()
    deletepa(fr2pw,userc,)
def deletepa(fr2pw,userc):
    global te
    te=StringVar(master=fr2pw)
    lbl1 = CTkLabel(fr2pw,text="Delete your package",text_color=TEXTS,font=("Nova Bomb SemBd", 35),)
    lbl1.place(y=50, relx=0.5, anchor="center")
    lbl2 = CTkLabel(fr2pw,text="Remove a package from your list",text_color=TEXTS,font=("Nova Bomb SemBd", 20),)
    lbl2.place(y=110, relx=0.5, anchor="center")
    fr = CTkFrame(fr2pw, fg_color=TEXTS, corner_radius=16, width=430, height=450)
    fr.place(relx=0.5, anchor="center", rely=0.6)
    lbl2 = CTkLabel(fr,text="Enter the tracking ID: ",text_color=FRAMES,font=("Nova Bomb SemBd", 25),)
    lbl2.place(y=50, relx=0.5, anchor="center")
    entry1 = CTkEntry(fr,placeholder_text="Enter your tracking ID",text_color=TEXTSE,placeholder_text_color=PLACETEXTS,corner_radius=16,fg_color=ENTRIE, width=250,height=40,font=("GROSTE", 20),border_width=0,textvariable=te)
    entry1.bind("<KeyRelease>", lambda  event:search(event,userc,frre))
    entry1.place(y=100,relx=0.5,anchor="center")
    btn1 = CTkButton(fr,text="View my package",fg_color=FRAMES,text_color=TEXTS,hover_color=HOVER,corner_radius=13,height=40,font=("Nova Bomb SemBd", 20),cursor="hand2",command=lambda:remove(userc,te))
    btn1.place(relx=0.5,anchor="center",rely=0.7)
    frre=CTkFrame(fr,fg_color=FRAMES, corner_radius=16, width=250, height=100)
    frre.place(relx=0.5,anchor="center",y=190)
    frre.pack_propagate(False)
    frre.place_forget()