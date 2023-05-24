import random
#Regla 1
l_p = {"p": None, "q":None , "r":None, "s":None, "t":None, "u":None, "x":None,
       "y":None, 'b':None, 'c':None}
T = [1, 2, 3, 4 ,5]
p1 = ["p", "q"]
r1 = random.choice(p1)
if r1 == "p":
    l_p['p'] = True
    l_p['q'] = False
else:
    l_p['q'] = True 
    l_p["p"] = False

p2 = ["s", "r"]
r2 = random.choice(p2)
if r2 == "s":
    l_p['s'] = True
    l_p['r'] = False
else: 
    l_p['r'] = True
    l_p["s"] = False
    
p3 = ["u", "t"]
r3 = random.choice(p3)
if r3 == "u":
    l_p['u'] = True
    l_p['t'] = False
else: 
    l_p['t'] = True
    l_p["u"] = False

p4= ["y", "x"]
r4 = random.choice(p4)
if r4 == "y":
    l_p['y'] = True
    l_p['x'] = False
else: 
    l_p['x'] = True
    l_p["y"] = False

p5 = ["b", "c"]
r5 = random.choice(p5)
if r5 == "b":
    l_p['b'] = True
    l_p['c'] = False
else: 
    l_p['c'] = True
    l_p["b"] = False
    
# print(r1)
# print(r2)
# print(r3)
# print(r4)
# print(r5)
print(l_p)

#Regla 2
#Regla 2
l_p = {"p": None, "q":None , "r":None, "s":None, "t":None, "u":None, "x":None,
       "y":None, 'b':None, 'c':None}

puente1 = [("p", T[0]), ("q", T[0])]
opc1 = random.choice(puente1)
print("La letra que escogio es:",opc1)

puente2 = [("s", T[0]), ("r", T[0])]
opc2 = random.choice(puente2)
print("La letra que escogio es:",opc2)

puente3 = [("u", T[0]), ("t", T[0])]
opc3 = random.choice(puente3)
print("La letra que escogio es:",opc3)

puente4 = [("y", T[0]), ("x", T[0])]
opc4 = random.choice(puente4)
print("La letra que escogio es:",opc4)

puente5 = [("b", T[0]), ("c", T[0])]
opc5 = random.choice(puente5)
print("La letra que escogio es:",opc5)
             
#Puente 1

print()
print("Puente 1")
if opc1 == ("p",T[0]):
        l_p["p"] = True
        l_p["q"] = False
        print("turno 1")
        print(l_p)
        for i in T:
            l = T[i]
            if l == 2:
                l_p["p"] = False
                l_p["q"] = False
                print("turno 2")
                print(l_p)
elif opc1 == ("q",T[0]):
        l_p["q"] = True
        l_p["p"] = False
        print("turno 1")
        print(l_p)
        for i in T:
            l = T[i]
            if l == 2:
                l_p["p"] = False
                l_p["q"] = False
                print("turno 2")
                print(l_p)

#Puente 2
print()
print("Puente 2")
if opc2 == ("s",T[0]):
        l_p["s"] = True
        l_p["r"] = False
        print("turno 1")
        print(l_p)
        for i in T:
            l = T[i]
            if l == 2:
                l_p["s"] = False
                l_p["r"] = False
                print("turno 2")
                print(l_p)
elif opc2 == ("r",T[0]):
        l_p["r"] = True
        l_p["s"] = False
        print("turno 1")
        print(l_p)
        for i in T:
            l = T[i]
            if l == 2:
                l_p["r"] = False
                l_p["s"] = False
                print("turno 2")
                print(l_p)

#Puente 3
print()
print("Puente 3")
if opc3 == ("u",T[0]):
        l_p["u"] = True
        l_p["t"] = False
        print("turno 1")
        print(l_p)
        for i in T:
            l = T[i]
            if l == 2:
                l_p["u"] = False
                l_p["t"] = False
                print("turno 2")
                print(l_p)
elif opc3 == ("t",T[0]):
        l_p["t"] = True
        l_p["u"] = False
        print("turno 1")
        print(l_p)
        for i in T:
            l = T[i]
            if l == 2:
                l_p["u"] = False
                l_p["t"] = False
                print("turno 2")
                print(l_p)

#Puente 4
print()
print("Puente 4")
if opc4 == ("y",T[0]):
        l_p["y"] = True
        l_p["x"] = False
        print("turno 1")
        print(l_p)
        for i in T:
            l = T[i]
            if l == 2:
                l_p["y"] = False
                l_p["x"] = False
                print("turno 2")
                print(l_p)
elif opc4 == ("x",T[0]):
        l_p["x"] = True
        l_p["y"] = False
        print("turno 1")
        print(l_p)
        for i in T:
            l = T[i]
            if l == 2:
                l_p["y"] = False
                l_p["x"] = False
                print("turno 2")
                print(l_p)

#Puente 5
print()
print("Puente 5")
if opc5 == ("b",T[0]):
        l_p["b"] = True
        l_p["c"] = False
        print("turno 1")
        print(l_p)
        for i in T:
            l = T[i]
            if l == 2:
                l_p["b"] = False
                l_p["c"] = False
                print("turno 2")
                print(l_p)
elif opc5 == ("c",T[0]):
        l_p["c"] = True
        l_p["b"] = False
        print("turno 1")
        print(l_p)
        for i in T:
            l = T[i]
            if l == 2:
                l_p["b"] = False
                l_p["c"] = False
                print("turno 2")
                print(l_p)

#la l indica el numero del turno.

#Regla 3

salidas = ("p","y","b")
inicial = (random.choice(salidas), T[0])

#print(inicial)

entradas = ('u', 's', 'y')
final = (random.choice(entradas), T[-1])
#print(final)


print("Si comienza en", inicial, "entonces termina en", final )

#puente  (A-C)
inter1 = {"p": True, "q":False , "r":False, "s":True, "t":False, "u":True, "x":True,
       "y":False, 'b':True, 'c':False}
inter2 = {"p": True, "q":False , "r":False, "s":True, "t":True, "u":False, "x":False,
       "y":True, 'b':False, 'c':True}
#puente (A_D)
inter3 = {"p": False, "q":True , "r":True, "s":False, "t":False, "u":True, "x":False,
       "y":True, 'b':True, 'c':False}
inter4 = {"p": True, "q":False , "r":False, "s":True, "t":False, "u":True, "x":True,
       "y":False, 'b':False, 'c':True}
#puente (A-B)
inter5 = {"p": True, "q":False , "r":False, "s":True, "t":False, "u":True, "x":True,
       "y":False, 'b':True, 'c':False}
inter6 = {"p": False, "q":True , "r":True, "s":False, "t":False, "u":True, "x":False,
       "y":True, 'b':True, 'c':False}




#Regla 4
l_p = {"p": None, "q":None , "r":None, "s":None, "t":None, "u":None, "x":None,
       "y":None, 'b':None, 'c':None}
puentes = [("p", T[0]), ("q", T[0]), ("s",T[0]), ("r", T[0]), ("u", T[0]), ("t", T[0]), ("y", T[0]), ("x", T[0]), ("b", T[0]), ("c", T[0])]
opc = random.choice(puentes)
print("La letra que escogio es:",opc)


if opc == ("p", T[0]):
    l_p["p"] = True
    l_p["q"] = False
    print("turno 1")
    print(l_p)
    for i in T:
        l = T[i]
        if l == 2:
            l_p["p"] = False
            l_p["s"] = True
            print("turno 2")
            print(l_p)

if opc == ("q", T[0]):
    l_p["q"] = True
    l_p["p"] = False
    print("turno 1")
    print(l_p)
    for i in T:
        l = T[i]
        if l == 2:
            camino = [("y", T[1]), ("b", T[1])]
            camino_escogido = random.choice(camino)
            if camino_escogido == ("y", T[1]):
                l_p["q"] = False
                l_p["y"] = True
                print("turno 2")
                print(l_p)
            elif camino_escogido == ("b", T[1]):
                l_p["q"] = False
                l_p["b"] = True
                print("turno 2")
                print(l_p)

if opc == ("s", T[0]):
    l_p["s"] = True
    l_p["r"] = False
    print("turno 1")
    print(l_p)
    for i in T:
        l = T[i]
        if l == 2:
            camino = [("x", T[1]), ("t", T[1])]
            camino_escogido = random.choice(camino)
            if camino_escogido == ("x", T[1]):
                l_p["s"] = False
                l_p["x"] = True
                print("turno 2")
                print(l_p)
            elif camino_escogido == ("t", T[1]):
                l_p["s"] = False
                l_p["t"] = True
                print("turno 2")
                print(l_p)

if opc == ("r", T[0]):
    l_p["r"] = True
    l_p["s"] = False
    print("turno 1")
    print(l_p)
    for i in T:
        l = T[i]
        if l == 2:
            l_p["r"] = False
            l_p["q"] = True
            print("turno 2")
            print(l_p)

if opc == ("u", T[0]):
    l_p["u"] = True
    l_p["t"] = False
    print("turno 1")
    print(l_p)
    for i in T:
        l = T[i]
        if l == 2:
            camino = [("x", T[1]), ("r", T[1])]
            camino_escogido = random.choice(camino)
            if camino_escogido == ("x", T[1]):
                l_p["u"] = False
                l_p["x"] = True
                print("turno 2")
                print(l_p)
            elif camino_escogido == ("r", T[1]):
                l_p["u"] = False
                l_p["r"] = True
                print("turno 2")
                print(l_p)

if opc == ("t", T[0]):
    l_p["t"] = True
    l_p["u"] = False
    print("turno 1")
    print(l_p)
    for i in T:
        l = T[i]
        if l == 2:
            l_p["t"] = False
            l_p["c"] = True
            print("turno 2")
            print(l_p)

if opc == ("y", T[0]):
    l_p["y"] = True
    l_p["x"] = False
    print("turno 1")
    print(l_p)
    for i in T:
        l = T[i]
        if l == 2:
            camino = [("t", T[1]), ("r", T[1])]
            camino_escogido = random.choice(camino)
            if camino_escogido == ("t", T[1]):
                l_p["y"] = False
                l_p["t"] = True
                print("turno 2")
                print(l_p)
            elif camino_escogido == ("r", T[1]):
                l_p["y"] = False
                l_p["r"] = True
                print("turno 2")
                print(l_p)

if opc == ("x", T[0]):
    l_p["x"] = True
    l_p["y"] = False
    print("turno 1")
    print(l_p)
    for i in T:
        l = T[i]
        if l == 2:
            camino = [("p", T[1]), ("b", T[1])]
            camino_escogido = random.choice(camino)
            if camino_escogido == ("p", T[1]):
                l_p["x"] = False
                l_p["p"] = True
                print("turno 2")
                print(l_p)
            elif camino_escogido == ("b", T[1]):
                l_p["x"] = False
                l_p["b"] = True
                print("turno 2")
                print(l_p)

if opc == ("c", T[0]):
    l_p["c"] = True
    l_p["b"] = False
    print("turno 1")
    print(l_p)
    for i in T:
        l = T[i]
        if l == 2:
            camino = [("y", T[1]), ("p", T[1])]
            camino_escogido = random.choice(camino)
            if camino_escogido == ("y", T[1]):
                l_p["c"] = False
                l_p["y"] = True
                print("turno 2")
                print(l_p)
            elif camino_escogido == ("p", T[1]):
                l_p["c"] = False
                l_p["p"] = True
                print("turno 2")
                print(l_p)

if opc == ("b", T[0]):
    l_p["b"] = True
    l_p["c"] = False
    print("turno 1")
    print(l_p)
    for i in T:
        l = T[i]
        if l == 2:
            l_p["b"] = False
            l_p["u"] = True
            print("turno 2")
            print(l_p) 
            
