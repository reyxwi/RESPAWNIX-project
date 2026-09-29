import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, BASE_DIR)
from _modules import *
from back_panel.card1 import *
from options.back import *
TEXTS = "#5A1E2A"
FRAMES = "#F7F1E5"
ENTRIE = "#89977D"
PLACETEXTS = "#5A1E2A"
def treeveiwa(fr2pw, userc):
    op = openj()
    re = reada(op, userc)
    st = ttk.Style()
    st.configure(
        "ty.Treeview",
        background=FRAMES,
        foreground=TEXTS,
        rowheight=40,
        font=("GROSTE", 14),
        borderwidth=0,
    )
    st.layout("ty.Treeview", [("Treeview.treearea", {"sticky": "nswe"})])
    st.configure(
        "Treeview.Heading",
        background=FRAMES,
        foreground=TEXTS,
        font=("Nova Bomb SemBd", 15),
    )
    t = ttk.Treeview(
        fr2pw,
        columns=("tracking", "reciever", "destenation", "Transpost", "status"),
        show="tree headings",
        style="ty.Treeview",
    )
    t.heading("tracking", text="Tracking ID")
    t.heading("reciever", text="Receiver")
    t.heading("destenation", text="Destenation")
    t.heading("Transpost", text="Transport")
    t.heading("status", text="Status")
    t.column("tracking", width=130)
    t.column("reciever", width=100)
    t.column("destenation", width=130)
    t.column("Transpost", width=80)
    t.column("status", width=100)
    icon = PhotoImage(file="assests/images/box (2).png")
    t.column("#0", width=50)
    for r in re:
        t.insert(
            "",
            "end",
            text="📦",
            values=(
                r["tracking"],
                r["reciever"],
                r["destenation"],
                r["Transpost"],
                r["status"],
            ),
            image=icon,
        )
    # t.place(relx=0.5, anchor="center", y=650, height=300, width=700)
    return t