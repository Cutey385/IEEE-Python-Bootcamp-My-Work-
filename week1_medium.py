x = float(input("1. sayıyı giriniz: "))
y = float(input("2. sayıyı giriniz: "))

toplam = x + y
fark = x - y
carpım = x * y
bolum = x / y

print(f"x + y = {toplam}\nx - y = {fark}\nx * y = {carpım}\n x / y = {bolum}\nx sayısı y sayısına tam bölünüyor mu : {x % y == 0} ")
