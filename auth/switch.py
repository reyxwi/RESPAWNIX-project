from auth.login import componentsfr1
from auth.signin import componentsfr1s


def switchlogin(fr1, window):
    for widget in fr1.winfo_children():
        widget.destroy()
    componentsfr1(fr1, switchsignin, window)


def switchsignin(fr1, window):
    for widget in fr1.winfo_children():
        widget.destroy()
    componentsfr1s(fr1, switchlogin, window)
