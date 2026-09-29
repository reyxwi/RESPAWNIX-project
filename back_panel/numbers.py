import json
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, BASE_DIR)
from _modules import *
from back_panel.card1 import *
pack=openj()
def reado(pack,userc):
    packs=[]
    for p in pack:
        if p["username"]==userc["username"]:
            if p["status"]=="on the way":
                packs.append(p)
    return packs
def reads(pack,userc):
    packs=[]
    for p in pack:
        if p["username"]==userc["username"]:
            if p["status"]=="sent":
                packs.append(p)
    return packs
def readd(pack,userc):
    packs=[]
    for p in pack:
        if p["username"]==userc["username"]:
            if p["status"]=="delivered":
                packs.append(p)
    return packs