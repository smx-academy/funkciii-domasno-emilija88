# Da se kreira funkcija plostina i funkcija perimetar koi ke primaat dva paremtri, 
# da presmetuvaat plostinata i perimetarot na pravoagolnik. 
# Korisnikot da gi vnesuva broevite i korisnikot da izbere koja presmetka da se izvrsi. 
# DA NE SE IZVRSUVAAT DVETE

def plostina(x, y):
    plo = x*y
    return plo

def perimetar(x, y):
    per = 2*x + 2*y
    return per

a = int(input("Vnesi prva strana: "))
b = int(input("Vnesi vtora strana: "))
plostina_kraj = plostina(a, b)
perimetar_kraj = perimetar(a, b)

while True:
    prasanje = input("Koja presmetka sakate da ja izvrshite? plostina ili perimetar?")
    if prasanje == "plostina":
        print("Plostinata na dadenite strani e {}.".format(plostina_kraj))
        break
    elif prasanje == "perimetar":
        print("Perimetarot na dadenite strani e {}.".format(perimetar_kraj))
        break
    else:
        print("Dadeniot odgovor ne odgovara na ponudenite presmetki.")
        continue


