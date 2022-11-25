# Da se kreira funkcija koja ke prima eden parametar lista i da moze da presmeta prosek na listata.

def lista(list):
    prosek_lista = sum(list) / len(list)
    return prosek_lista


lista1 = []
n = int(input("Vnesete kolku broevi sakate da sodrzi vasata lista?"))
for x in range(n):
    x = int(input("Vnesete broj: "))
    lista1.append(x)

lista_kraj = lista(lista1)
print("Prosekot na vashata lista e {}.".format(lista_kraj))




    
