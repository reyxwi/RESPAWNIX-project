import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, BASE_DIR)
from options.back import *
from _modules import *
from adminpanel.dashboarda import *
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
def spanned(window,userc):
    n=userc["name"]
    fr=CTkFrame(window,width=900,height=50,fg_color=TEXTS)
    fr.place(x=50,y=0)
    lbl=CTkLabel(fr,text="RESPAWNIX",text_color=FRAMES,font=("Pixel O10 Bott",20))
    lbl.place(y=0,x=20)
    lbl1=CTkLabel(fr,text=f"ADMIN * {n}",text_color=FRAMES,font=("Nova Bomb SemBd",20))
    lbl1.place(y=0,x=800)
    pw=PanedWindow(window,orient="horizontal",bg=FRAMES,sashwidth=5)
    pw.place(relx=0.5,rely=0.5,anchor="center")
    return pw
def setframes(pw:PanedWindow):
    fr1pw=CTkFrame(pw,height=580,width=460,corner_radius=16,fg_color=TEXTS)
    fr2pw=CTkFrame(pw,height=580,width=460,corner_radius=16,fg_color=FRAMES)
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
    btn2=CTkButton(fr1pw,text="Package",font=("Nova Bomb SemBd",20),text_color=TEXTS,fg_color=FRAMES,hover_color=HOVER,corner_radius=16,cursor="hand2",width=170,height=50)
    btn2.place(relx=0.5,anchor="center",y=300)
    btn3=CTkButton(fr1pw,text="Search",font=("Nova Bomb SemBd",20),text_color=TEXTS,fg_color=FRAMES,hover_color=HOVER,corner_radius=16,cursor="hand2",width=170,height=50)
    btn3.place(relx=0.5,anchor="center",y=370)
    btn4=CTkButton(fr1pw,text="Statistics",font=("Nova Bomb SemBd",20),text_color=TEXTS,fg_color=FRAMES,hover_color=HOVER,corner_radius=16,cursor="hand2",width=170,height=50)
    btn4.place(relx=0.5,anchor="center",y=440)
def run(window,userc):
    # window=swindowp()
    pw=spanned(window,userc)
    window.configure(fg_color=FRAMES)
    fr1pw,fr2pw=setframes(pw)
    chnage1=chnageframe1(fr1pw)
    btnfr1=buttonsfr1(fr1pw,fr2pw,userc,window)
    d=dash(fr2pw,userc)
    # window.mainloop()
