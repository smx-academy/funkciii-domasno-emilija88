# Da se kreira funkcija so ime zbir koja ke prima dva broevi kako parametar, 
# da se presmeta zbirot i 
# da se ispecati dali zbirot e paren ili ne paren. 
# Broevite da gi vnese korisnikot.

def zbir(x, y):
    sobiranje = x+y
    return sobiranje

a = int(input("Vnesi eden broj: "))
b = int(input("Vnesi uste eden broj: "))
sobiranje_zbir = zbir(a, b)
print(sobiranje_zbir)

if sobiranje_zbir % 2 == 0:
    print("Zbirot na dvata broja e paren.")
else:
    print("Zbirot na dvata broja e neparen.")
