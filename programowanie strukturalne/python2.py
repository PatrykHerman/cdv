tekst = "Anna, paweł, Tomek"

tab = tekst.split(",")
print(tekst)
print(tab)
imie = tab[0]
print(imie)
print(type(tab))

imieDuze = imie.upper()
print(imieDuze)

imieMale = imie.lower()
print(imieMale)

#sprzawdzanie zawartosci
zawartosc = imie.isalpha()
print(zawartosc)
print(type(zawartosc))

imie = ""
zawartosc = imie.isalpha()
print(zawartosc)
print(type(zawartosc))