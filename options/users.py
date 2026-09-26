import os
import sys
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0,BASE_DIR)
from _modules import *
from validation.validation import *
from validation.empty import *
TEXTS="#5A1E2A"
FRAMES="#F7F1E5"
ENTRIE="#89977D"
PLACETEXTS="#5A1E2A"
HOVER="#6F7C63"
def add(name,username,password):
    with open("data/role.json", "r") as file:
        users=json.load(file)
    res=checksign(name,username,password,users)
    if res==False:
        return False
    user={
        "name":name,
        "username":username,
        "password":password,
        "role":"user"
        } 
    users.append(user)
    with open("data/role.json","w") as file:
        json.dump(users,file)
    return True
    