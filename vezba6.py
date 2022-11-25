# Da se kreira funkcija so ime najdolgo ime koja ke prima lista kako parametar, 
# da go njade najdolgoto ime od lista, 
# da go ispecati i da kaze od kolku karakteri e sostaveno. 
# Korisnikot da gi vnesuva iminjata

def najdolgo_ime(list):
    dolzina_lista = max(list, key=len)
    return dolzina_lista


lista5 = []
n = int(input("Vnesete kolku iminja sakate da sodrzi vasata lista?"))
for x in range(n):
    x = input("Vnesete ime: ")
    lista5.append(x)

lista_na_iminja = najdolgo_ime(lista5)
print("Najdolgoto ime na vashata lista e {}.".format(lista_na_iminja))

brojka = len(lista_na_iminja)
print("Imeto e sostaveno od {} bukvi.".format(brojka))

