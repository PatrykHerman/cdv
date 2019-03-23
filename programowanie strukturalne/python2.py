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

imie = "Julia"
print("\nDane uzytkownika: \nMasz na imie: " + imie)

text1 = "Jan\n"
text2 = "Nowak"
print(text1 + text2)

text = text1.rstrip()
print(text1 + " " + text2)

#wyswietlanie ciagu znakow
#wszystkie wersje pythona

text = "%s, Java i %s "%("PHP","Python")
print(text)

#nowsze wersje pythona 2.6
text = "(0), Java i (1)".format("PHP","Python")
print(text)

#help(text.replace)

new = text.replace("PHP", "C#")
print(new)

#wypisywanie danych
rok = "2019"
miesiac = "marzec"
dzien = "23"

print("Data: ", end="")
print(dzien, miesiac, rok)

print("Data: ", end="")
print(dzien, miesiac, rok, sep="-")









