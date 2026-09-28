import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, BASE_DIR)
from _modules import *
def load_photo(PATH: str, window, size=None, bg=None, widget="label",hover=None,widthb=None,heightb=None,commnd=None,corner=None):
    I = Image.open(PATH)
    if size != None:
        I = I.resize(size=size)
    photo_back = CTkImage(light_image=I,dark_image=I,size=size
)
    match widget:
        case "label":
            if bg != None:
                bg_img = CTkLabel(window, image=photo_back, fg_color=bg,text="",corner_radius=corner)
            else:
                bg_img = CTkLabel(window, image=photo_back,text="",corner_radius=corner)
            # buffer memory ON
            bg_img.image = photo_back
            return bg_img
        case "button":
            if bg != None:
                bg_img = CTkButton(
                    window,
                    image=photo_back,
                    fg_color=bg,
                    text="",
                    hover_color=hover,
                    width=widthb,
                    height=heightb,
                    command=commnd,
                    corner_radius=corner
                )
            else:
                bg_img = CTkButton(window, image=photo_back,corner_radius=corner)
            bg_img.image = photo_back
            return bg_img
def spassword(entry3,password):
    if password.get()=="*":
        entry3.configure(show="")
        password.set("")
    else:
        entry3.configure(show="*")
        password.set("*")
