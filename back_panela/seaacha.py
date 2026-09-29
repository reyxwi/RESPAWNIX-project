import os
import sys
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0,BASE_DIR)
from _modules import *
from options.back import *
from back_panel.card1 import *
FRAMES="#5A1E2A"
TEXTS="#F7F1E5"
ENTRIE="#89977D"
PLACETEXTS="#5A1E2A"
HOVER="#6F7C63"
def se(s_var,userc,tr,event):
    srch=s_var.get()
    op=openj()
    read=reada(op,userc)
    res=[]
    for r in read:
        if srch in r["tracking"]:
            res.append(r)
    for i in tr.get_children():
        tr.delete(i)
    for r in res:
        tr.insert(
            "",
            "end",
            text="📦",
            values=(
                r["tracking"],
                r["reciever"],
                r["destenation"],
                r["Transpost"],
                r["status"],
            )
            )