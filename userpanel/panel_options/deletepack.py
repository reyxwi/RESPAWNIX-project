import os
import sys
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0,BASE_DIR)
from _modules import *
from options.back import *
from options.jpack import remove2

TEXTS="#353535"
FRAMES="#DFDDD7" 
ENTRIE = "#E9F9DB"
HOVER="#6F7C63"
def tdelpack():
    top=CTkToplevel()
    top.geometry("520x580")
    top.resizable(False,False)
    top.overrideredirect(True)
    top.attributes("-topmost", True)
    top.configure(fg_color=TEXTS)
    return top
def setfra(top,pgk):
    tr=pgk["tracking"]
    lbl1 = CTkLabel(top,text="Package Found",text_color=FRAMES,font=("Nova Bomb SemBd", 35),)
    lbl1.place(y=50, relx=0.5, anchor="center")
    lbl2 = CTkLabel(top,text=f" 📦 {tr}",text_color=FRAMES,font=("Nova Bomb SemBd", 25),)
    lbl2.place(y=150, relx=0.5, anchor="center")
    lbl2 = CTkLabel(top,text="────────────────",text_color=FRAMES,font=("Nova Bomb SemBd", 25),)
    lbl2.place(y=200, relx=0.5, anchor="center")
    fr = CTkFrame(top, fg_color=FRAMES, corner_radius=16, width=130, height=130)
    fr.place(relx=0.15,rely=0.4)
    fr2 = CTkFrame(top, fg_color=FRAMES, corner_radius=16, width=130, height=130)
    fr2.place(relx=0.6,rely=0.4)
    fr3 = CTkFrame(top, fg_color=FRAMES, corner_radius=16, width=130, height=130)
    fr3.place(relx=0.15,rely=0.65)
    fr4 = CTkFrame(top, fg_color=FRAMES, corner_radius=16, width=130, height=130)
    fr4.place(relx=0.6,rely=0.65)
    return fr,fr2,fr3,fr4
def setcom(top,pgk,fr,fr2,fr3,fr4):
    r=pgk["reciever"]
    t=pgk["Transpost"]
    d=pgk["destenation"]
    s=pgk["status"]
    lbl=CTkLabel(fr,text=f"Reciever: \n\n {r}",text_color=TEXTS,font=("GROSTE", 15),)
    lbl.place(x=20,y=30)
    lbl2=CTkLabel(fr2,text=f"destenation: \n\n {d}",text_color=TEXTS,font=("GROSTE", 15),)
    lbl2.place(x=20,y=30)
    lbl2=CTkLabel(fr2,text=f"Transport: \n\n {t}",text_color=TEXTS,font=("GROSTE", 15),)
    lbl2.place(x=20,y=30)
    lbl3=CTkLabel(fr3,text=f"Transport: \n\n {t}",text_color=TEXTS,font=("GROSTE", 15),)
    lbl3.place(x=20,y=30)
    lbl4=CTkLabel(fr4,text=f"status: \n\n {s}",text_color=TEXTS,font=("GROSTE", 15),)
    lbl4.place(x=20,y=30)
    btn1 = CTkButton(top,text="Delete",fg_color=FRAMES,text_color=TEXTS,hover_color=HOVER,corner_radius=13,height=40,font=("Nova Bomb SemBd", 20),cursor="hand2",command=lambda:remove2(pgk))
    btn1.place(relx=0.5,anchor="center",rely=0.95)
    btn2 = CTkButton(top,text="❌",fg_color=TEXTS,text_color=FRAMES,hover_color=HOVER,corner_radius=13,height=40,font=("Nova Bomb SemBd", 20),cursor="hand2",width=20,command=lambda:destroy(top))
    btn2.place(relx=0.85,y=20)
def destroy(top: CTkToplevel):
    top = top.winfo_toplevel()
    top.destroy()

def rund(pgk):
    top=tdelpack()
    fr,fr2,fr3,fr4=setfra(top,pgk)
    c=setcom(top,pgk,fr,fr2,fr3,fr4)
    top.mainloop()



    
