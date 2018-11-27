import math

def newtonPi(init):
    x0 = init
    x1 = x0 - (math.sin(x0)/math.cos(x0))
    a = True
    while a:
        x0 = x1
        x1 = x0 - (math.sin(x0)/math.cos(x0))
        a = x0 != x1
    return x0


def leibnizPi(iterations):
    plusminus = 1.0
    secteni = 0.0
    for k in range(iterations):
        secteni += plusminus / (2 * k + 1)
        plusminus *= -1

    return 4 * secteni

def nilakanthaPi(iterations):
    secteni2 = 0.0
    k = 2
    for x in range (iterations):
        if secteni2 == 0:
            vysledek = 3
            secteni2 = secteni2 + vysledek
        elif x > 0:
            k = (-1)**(x+1) / ((k)*(k + 1)* (2 + k))
            n = 4 * k
            secteni2 = secteni2 + (n)
            k = (k-(k-2*(x+1)))
            
    return secteni2






    