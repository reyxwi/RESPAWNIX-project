from options.userlog import checkuser
from userpanel.upanel import run
from options.users import add
def login(window,username, role, password):
    userc= checkuser(username, role, password)
    if userc:
        run(window,userc)
        return userc
def signup(window,name,username,password):
    userc= add(name,username,password)
    if userc:
        userc= {
        "name":name,
        "username":username,
        "password":password,
        "role": "user"}
        run(window,userc)