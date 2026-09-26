import random
def addpgk(userc,reciever,dest,tran):
    trn=f"RPX-{random.randint(1000,9999)}-{random.randint(10,99)}"
    pgk={"tracking":trn,
        "username":userc["username"],
        "name":userc["name"],
        "reciever":reciever,
        "destenation":dest,
        "Transpost":tran,
        "status":"unknown"}
    return pgk