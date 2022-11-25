# Da se napravi funkcija koja kako parametar ke prima nekoj string i da proveri dali toj string e palindrom 
# t.e. dali toj string se cita od dvete strani na primer: ana, kalabalak

def dali_palindrom(zbor):
    return zbor == zbor[::-1]

zbor = input("Vnesi zbor: ")
x = dali_palindrom(zbor)
 
if x:
    print("Da")
else:
    print("Ne")