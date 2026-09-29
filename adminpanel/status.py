import os
import sys
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0,BASE_DIR)
from _modules import *
from back_panel.card1 import *
from adminpanel.tree import *
FRAMES="#5A1E2A"
TEXTS="#F7F1E5"
ENTRIE="#89977D"
PLACETEXTS="#5A1E2A"
HOVER="#6F7C63"
def select(event,lbl2):
    tr=event.widget
    s=tr.selection()
    d=tr.item(s)
    tra=d["values"][0]
    lbl2.configure(text=tra)
def cleanfr2(fr2pw,userc):
    for f in fr2pw.winfo_children():
        f.destroy()
    setsta(fr2pw,userc)
def setsta(fr2pw,userc):
    st=StringVar(value="")
    tr=treeveiwa(fr2pw,userc)
    tr.place(relx=0.5, anchor="center", y=200, height=200, width=700)
    lbl=CTkLabel(fr2pw,text="📦 Select a package ",text_color=FRAMES,font=("Nova Bomb SemBd",40))
    lbl.place(y=50,relx=0.5,anchor="center")
    lbl1=CTkLabel(fr2pw,text="📦 Selected Package ",text_color=FRAMES,font=("Nova Bomb SemBd",20))
    lbl1.place(y=280,relx=0.5,anchor="center")
    fr=CTkFrame(fr2pw,width=600,height=300,fg_color=FRAMES,corner_radius=16)
    fr.place(y=440,relx=0.5,anchor="center")
    fr.pack_propagate(False)
    lbl2=CTkLabel(fr,text="",text_color=TEXTS,font=("Nova Bomb SemBd",20))
    lbl2.place(y=50,relx=0.5,anchor="center")
    tr.bind("<<TreeviewSelect>>",lambda event:select(event,lbl2))
    lbl3=CTkLabel(fr,text="choose a status",text_color=TEXTS,font=("Nova Bomb SemBd",20))
    lbl3.place(y=80,relx=0.5,anchor="center")
    btn1=CTkButton(fr,text="on the way",font=("Nova Bomb SemBd",20),text_color=FRAMES,fg_color="#a9e8a7",hover_color=HOVER,corner_radius=16,cursor="hand2",width=150,height=50,command=lambda:st.set("on the way"))
    btn1.pack(padx=30,pady=50,side="left")
    btn2=CTkButton(fr,text="Delivered",font=("Nova Bomb SemBd",20),text_color=FRAMES,fg_color="#e6e8a7",hover_color=HOVER,corner_radius=16,cursor="hand2",width=150,height=50,command=lambda:st.set("delivered"))
    btn2.pack(padx=30,pady=50,side="left")
    btn3=CTkButton(fr,text="sent",font=("Nova Bomb SemBd",20),text_color=FRAMES,fg_color="#b8bbc2",hover_color=HOVER,corner_radius=16,cursor="hand2",width=150,height=50,command=lambda:st.set("sent"))
    btn3.pack(padx=30,pady=50,side="left")
    btn4=CTkButton(fr,text="Change",font=("Nova Bomb SemBd",20),text_color=FRAMES,fg_color=TEXTS,hover_color=HOVER,corner_radius=16,cursor="hand2",width=150,height=50,command=lambda:change(st,tr))
    btn4.place(relx=0.5,anchor="center",y=250)
    return tr
def change(st,tr):
    s=tr.selection()
    d=tr.item(s)
    tra=d["values"][0]
    new=st.get()
    packs=openj()
    for p in packs:
        if p["tracking"]==tra:
            p["status"]=new   
    with open("data/packages.json","w") as file:
        json.dump(packs,file)