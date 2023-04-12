import random
def r1():
    w = int(input("Количество поролий"))
    e = int(input("количество символов"+"/n"))
    sim = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    for A in range(w):
        pas = ""
        for B in range(w):
            pas += random.choice(sm)
        print(pas)

