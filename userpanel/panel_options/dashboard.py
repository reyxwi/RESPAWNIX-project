import os
import sys
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0,BASE_DIR)
from _modules import *
from options.back import *
from userpanel.time import *
from back_panel.card1 import *
from userpanel.panel_options.treeveiw import *
from userpanel.panel_options.search import se
FRAMES="#5A1E2A"
TEXTS="#F7F1E5"
ENTRIE="#89977D"
PLACETEXTS="#5A1E2A"
HOVER="#6F7C63"
ti=good()
def cleanfr2pwd(fr2pw,userc):
    for f in fr2pw.winfo_children():
        f.destroy()
    dash(fr2pw,userc)
def dash(fr2pw,userc):
    n=userc["name"]
    us=userc["username"]
    s_var=StringVar()
    # lbl=CTkLabel(fr2pw,text="RESPAWNIX",text_color=FRAMES,font=("Pixel O10 Bott",35))
    # lbl.place(x=450,y=30)
    u=load_photo("assests/images/user.png",fr2pw,(45,45),widget="label")
    u.place(x=600,y=38)
    lbl=CTkLabel(fr2pw,text=us,text_color=FRAMES,font=("Nova Bomb SemBd",20))
    lbl.place(y=40,x=650)
    lbl1=CTkLabel(fr2pw,text=f"{ti} {n}",text_color=FRAMES,font=("Nova Bomb SemBd",40))
    lbl1.place(x=50,y=40)
    lbl1=CTkLabel(fr2pw,text="Here is your package review",text_color=FRAMES,font=("Nova Bomb SemBd",20))
    lbl1.place(x=50,y=100)
    entry=CTkEntry(fr2pw,fg_color=TEXTS,text_color=FRAMES,placeholder_text="search your post... ",placeholder_text_color=PLACETEXTS,border_color=PLACETEXTS,border_width=3,font=("GROSTE",15),width=200,height=50,corner_radius=16,textvariable=s_var)
    entry.place(x=390,y=40)
    entry.bind("<KeyRelease>", lambda event: se(s_var, userc,tr,event))
    tr=cards3(fr2pw,userc)
def cards3(fr2pw,userc):
    pack=openj()
    packs=len(readj(pack,userc))
    stu=len(un(pack,userc))
    fr1=CTkFrame(fr2pw,corner_radius=13,width=130,height=130,fg_color=TEXTS,border_color=FRAMES,border_width=3)
    fr1.place(x=30,y=170)
    fr2=CTkFrame(fr2pw,corner_radius=16,width=130,height=130,fg_color=TEXTS,border_color=FRAMES,border_width=3)
    fr2.place(x=200,y=170)
    fr3=CTkFrame(fr2pw,corner_radius=16,width=130,height=130,fg_color=TEXTS,border_color=FRAMES,border_width=3)
    
    fr3.place(x=370,y=170)
    fr4=CTkFrame(fr2pw,corner_radius=16,width=130,height=130,fg_color=TEXTS,border_color=FRAMES,border_width=3)
    fr4.place(x=540,y=170)
    lbl=CTkLabel(fr1,text="All packages",text_color=FRAMES,font=("Pixelhands",15))
    lbl.place(y=100,relx=0.5,anchor="center")
    lbl1=CTkLabel(fr2,text="On the way",text_color=FRAMES,font=("Pixelhands",15))
    lbl1.place(y=100,relx=0.5,anchor="center")
    lbl2=CTkLabel(fr3,text="Delivered",text_color=FRAMES,font=("Pixelhands",15))
    lbl2.place(y=100,relx=0.5,anchor="center")
    lbl3=CTkLabel(fr4,text="Unknown",text_color=FRAMES,font=("Pixelhands",15))
    lbl3.place(y=100,relx=0.5,anchor="center")
    tick=load_photo("assests/images/tick.png",fr1,(35,35),widget="label",corner=30)
    tick.place(y=20,x=10)
    track=load_photo("assests/images/track.png",fr2,(35,35),widget="label",corner=30)
    track.place(y=20,x=10)
    clock=load_photo("assests/images/clock.png",fr3,(35,35),widget="label",corner=30)
    clock.place(y=20,x=10)
    que=load_photo("assests/images/que.png",fr4,(35,35),widget="label",corner=30)
    que.place(y=20,x=10)
    lbl3=CTkLabel(fr1,text=packs,text_color=FRAMES,font=("Pixelhands",30))
    lbl3.place(y=50,x=90)
    lbl4=CTkLabel(fr2,text="",text_color=FRAMES,font=("Pixelhands",30))
    lbl4.place(y=50,x=90)
    lbl5=CTkLabel(fr3,text="",text_color=FRAMES,font=("Pixelhands",30))
    lbl5.place(y=50,x=90)
    lbl6=CTkLabel(fr4,text=stu,text_color=FRAMES,font=("Pixelhands",30))
    lbl6.place(y=50,x=90)
    tr=treeveiw(fr2pw,userc)
    return tr