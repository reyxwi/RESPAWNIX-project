import os
import sys
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0,BASE_DIR)
from _modules import *
from auth.signin import setwindow, frames
from auth.signin import componentsfr1s, componentsfr2
from auth.switch import switchlogin
window=setwindow()
fr1,fr2=frames(window)
componentsfr1s(fr1, switchlogin,window)
componentsfr2(fr2)
window.mainloop() 