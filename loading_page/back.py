import os
import sys
import time
import random
base_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, base_dir)
from _modules import *
count = 0
def loading_progress(progressbar: CTkProgressBar, txt_lbl: CTkLabel ,window: CTk,next,mwindow,userc):
    global count
    count += 1
    if count <= 100:
        txt = f"Loading {count}%"
        progressbar.set(count / 100)
        txt_lbl.configure(text=txt)
        window.after(
            random.randint(1, 100), loading_progress, progressbar, txt_lbl, window,next,mwindow,userc)
    else:
        
        window.destroy()
        mwindow.deiconify()
        next(mwindow,userc)