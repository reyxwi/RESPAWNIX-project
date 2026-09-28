import os
import sys
base_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, base_dir)
from _modules import *
from loading_page.back import *
from options.back import *
TEXTS="#5A1E2A"
FRAMES="#FFFFFF"
ENTRIE="#89977D"
PLACETEXTS="#5A1E2A"
HOVER="#6F7C63"
def swindow():
    window = CTkToplevel()
    window.resizable(False, False)
    height = 330
    width = 430
    y = (window.winfo_screenheight() // 2) - (height // 2)
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    window.overrideredirect(True)
    window.geometry(f"{width}x{height}+{x}+{y}")
    window.configure(fg_color=FRAMES)
    return window
def animate(window, gif, label):
    try:
        frame = gif.copy()
        frame.thumbnail((150, 150))
        frame = ImageTk.PhotoImage(frame)
        label.configure(image=frame)
        label.image = frame
        gif.seek(gif.tell()+ 1)
        window.after(50, animate,window,gif,label)
    except EOFError:
        gif.seek(0)
        window.after(50, animate, window,gif,label)
def loading_gif(window):
    gif = Image.open("assests/images/loading.gif")

    label = CTkLabel(window, text="")
    label.place(relx=0.5,rely=0.5,anchor="center")

    animate(window, gif, label)
def setcompo(window):
    p=load_photo("assests/images/banner2.png",window,(200,200),widget="label")
    p.place(relx=0.5,anchor="center",y=30)
    lbl=CTkLabel(window,text="please wait...",text_color=TEXTS,font=("Nova Bomb SemBd",20))
    lbl.place(relx=0.5,anchor="center",rely=0.7)
    txt_lbl = CTkLabel(window, text="", font=("Nova Bomb SemBd",20),text_color=TEXTS,)
    txt_lbl.place(anchor="center", relx=0.5, rely=0.9)
    progressbar = CTkProgressBar(window,width=400,progress_color=TEXTS,fg_color=FRAMES,height=20,corner_radius=16)
    progressbar.place(anchor="center", relx=0.5, rely=0.8)
    return progressbar,txt_lbl
def run(next, window, userc):
    lwindow=swindow()
    loading_gif(lwindow)
    progressbar,txt_lbl=setcompo(lwindow)
    loading_progress(progressbar, txt_lbl, lwindow,next,window,userc)
    lwindow.mainloop()
