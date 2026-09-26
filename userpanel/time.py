import datetime as dt
def good():
    now=dt.datetime.now().hour
    if now<12:
        return "good morning ☀️"
    elif now<18:
        return "Good afternoon ⛅"
    else:
        return "Good night 🌙"
