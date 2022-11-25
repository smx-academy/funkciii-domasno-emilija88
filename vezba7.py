# Da se napravi funkcija koja ke presmetuva prosek na ucenik, 
# otcenite da gi prima kako parametar vo lista. 
# Da ima druga funkcija koja kako parametri ke gi prima prosekot i imeto na ucenikot, 
# ke presmetuva uspeh na ucenik spored prosekot i da ispecati so kakov uspeh e toj ucenik

def prosek(ocena):
    return sum(ocena)/len(ocena)

def prosek2(ime, average):
    resenie = ("{} ima prosek {}.".format(ime, average))
    return(resenie)
    
ocenki = []
y = input("Vnesi ime: ")
for x in range(5):
    x = int(input("Vnesi ocenka: "))
    ocenki.append(x)
average=(prosek(ocenki))
score=(prosek2(y, average))
print(score)

if average >0 and average <=1.5 :
    print("Uspehot na uchenikot e nezadovolitelen.".format(average))
elif average >1.5 and average <=2.5:
    print("Uspehot na uchenikot e dovolen.".format(average))
elif average >2.5 and average <=3.5:
    print("Uspehot na uchenikot e dobar.".format(average))
elif average >3.5 and average <=4.5:
    print("Uspehot na uchenikot e mnogu dobar.".format(average))
elif average >4.5 and average <=5.5:
    print("Uspehot na uchenikot e odlicen.".format(average))

