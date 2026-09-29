import os
import sys
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0,BASE_DIR)
from _modules import *
FRAMES="#5A1E2A"
TEXTS="#F7F1E5"
ENTRIE="#89977D"
PLACETEXTS="#5A1E2A"
HOVER="#6F7C63"
def cleanfc(fr2pw,userc,on,de,s,stu):
    for f in fr2pw.winfo_children():
        f.destroy()
    chart(fr2pw,on,de,s,stu)
def chart(fr2pw,on,de,s,stu):
    fi=plt.Figure(figsize=(5, 4),facecolor=TEXTS)
    a=fi.add_subplot(111)
    lbs=["on the way", "delivered","sent","unknown"]
    val=[on, de, s, stu]
    a.pie(val,labels=lbs,colors=["#a9e8a7","#e6e8a7","#b8bbc2","#8e6e6e"],textprops={"fontsize": 12,"fontname": "Arial","color":FRAMES})
    ca=FigureCanvasTkAgg(fi, master=fr2pw)
    ca.draw()
    ca.get_tk_widget().place(relx=0.5,anchor="center",rely=0.5)
