import os
import sys
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0,BASE_DIR)
from _modules import *
from options.back import *
from userpanel.panel_options.dashboard import *
from userpanel.panel_options.addp import *
from userpanel.panel_options.delete import *

TEXTS="#5A1E2A"
FRAMES="#F7F1E5"
ENTRIE="#89977D"
PLACETEXTS="#5A1E2A"
HOVER="#6F7C63"
def swindowp():
    window=CTk()
    window.geometry("1000x650")
    window.resizable(False,False)
    window.configure(fg_color=FRAMES)
    window.title("My panel")
    return window
def spanned(window):
    pw=PanedWindow(window,orient="horizontal",bg=FRAMES,sashwidth=5)
    pw.place(relx=0.5,rely=0.5,anchor="center")
    return pw
def setframes(pw:PanedWindow):
    fr1pw=CTkFrame(pw,height=600,width=460,corner_radius=16,fg_color=TEXTS)
    fr2pw=CTkFrame(pw,height=600,width=460,corner_radius=16,fg_color=FRAMES)
    pw.add(fr1pw)
    pw.add(fr2pw)
    pw.sash_place(0,250,0)
    return fr1pw,fr2pw
def chnageframe1(fr1pw):
    bn=load_photo("assests/images/banner.png",fr1pw,(150,150),widget="label")
    bn.place(y=10,x=30)
    lbl2=CTkLabel(fr1pw,text="─────────────────────",text_color=FRAMES,font=("Arial",15),border_width=3,border_color=FRAMES)
    lbl2.place(y=150,relx=0.5,anchor="center")
def buttonsfr1(fr1pw,fr2pw,userc,window):
    btn1=CTkButton(fr1pw,text="Dashboard",font=("Nova Bomb SemBd",20),text_color=TEXTS,fg_color=FRAMES,hover_color=HOVER,corner_radius=16,cursor="hand2",width=170,height=50,command=lambda:cleanfr2pwd(fr2pw,userc))
    btn1.place(relx=0.5,anchor="center",y=230)
    btn2=CTkButton(fr1pw,text="Add Packages",font=("Nova Bomb SemBd",20),text_color=TEXTS,fg_color=FRAMES,hover_color=HOVER,corner_radius=16,cursor="hand2",width=170,height=50,command=lambda:cleanfr2pw(fr2pw,userc))
    btn2.place(relx=0.5,anchor="center",y=300)
    btn3=CTkButton(fr1pw,text="Delete package",font=("Nova Bomb SemBd",20),text_color=TEXTS,fg_color=FRAMES,hover_color=HOVER,corner_radius=16,cursor="hand2",width=170,height=50,command=lambda:cleanfde(fr2pw,userc))
    btn3.place(relx=0.5,anchor="center",y=370)
    # bn1=load_photo("assests/images/log.png",fr1pw,(20,20),widget="label")
    # bn1.place(relx=0.25,anchor="center",y=550)
    # btn4=CTkButton(fr1pw,text="Log out",font=("Nova Bomb SemBd",15),text_color=FRAMES,hover_color=HOVER,corner_radius=16,cursor="hand2",fg_color=TEXTS,width=20,command=lambda)
    # btn4.place(relx=0.5,anchor="center",y=550)
def run(window,userc):
    # window=swindowp()
    pw=spanned(window)
    window.configure(fg_color=FRAMES)
    fr1pw,fr2pw=setframes(pw)
    chnage1=chnageframe1(fr1pw)
    btnfr1=buttonsfr1(fr1pw,fr2pw,userc,window)
    d=dash(fr2pw,userc)
    # window.mainloop()
