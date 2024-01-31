ad = input("Ad: ")
soyad = input("Soyad: ")
CRN = int(input("CRN: "))
ders = input("Ders Adı: ")
vize1 = float(input("Birinci vize notunuz: "))
vize2 = float(input("İkinci vize notunuz: "))
final = float(input("Final notunuz: "))

ort = round((0.3 * vize1 + 0.3 * vize2 + 0.4 * final),1)

print(f"Okulumuz öğrencilerinden {ad.title()} {soyad.capitalize()}, {CRN}-{ders.upper()} dersinden {ort} ortalamaya sahiptir.")



