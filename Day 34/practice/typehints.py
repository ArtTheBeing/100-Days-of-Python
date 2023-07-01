age: int
name: str
heigh: float
#You can set a certain datatype

def police_check(age: int) -> bool:  #The arrow pointin to data type shows what is expected to return
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

#You can also do it for functions