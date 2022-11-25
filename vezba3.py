# Da se kreira funkcija so ime najgolem_broj koja ke prima 3 parametri, 
# da se najde najgolemiot broj i da se ispecati. 
# Broevite da gi vnese korisnikot

def najgolem_broj(a, b, c):
    rezultat = max(a, b, c)
    return rezultat

x = int(input("Vnesi prv broj: "))
y = int(input("Vnesi vtor broj: "))
z = int(input("Vnesi tret broj: "))
krajno = najgolem_broj(x, y, z)
print("Najgolem od broevite koi gi vnesovte e brojot {}.".format(krajno))