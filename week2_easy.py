baskentler = {
    "Türkiye" : "Ankara",
    "Rusya": "Moskova",
    "Azerbaycan" : "Bakü"
}

bos_liste = []

for key, value in baskentler.items():
   bos_liste.append(key)
   bos_liste.append(value)

i = len(bos_liste) - 1

while i >= 0 :
    print(bos_liste[i])
    i = i-1