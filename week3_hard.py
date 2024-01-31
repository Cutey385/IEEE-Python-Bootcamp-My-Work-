def main():
    n = int(input("Otoparkın Bir Kenar Uzunluğu: "))
    otopark = otopark_olustur(n)
    print(f"Otopark:\n{otopark_ciz(otopark)}")
    #while True:
     #   try:
      #      cevap = int(input("Eklenecek Araç Sayısı Girin:"))
       #     arac_ekle(otopark, cevap)
        #    print(f"Otopark:\n{otopark_ciz(otopark)}")
        #except ValueError:
         #   print("Geçerli bir değer girilmedi! İşlem iptal ediliyor..")
          #  break
        #except:
         #   print("Hata! İşlem iptal ediliyor...")
          #  break

def otopark_olustur(n):
    otopark = []
    rows, cols = (n, n)
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(0)
        otopark.append(col)
    return otopark
    
def otopark_ciz(otopark):
    image = ""
    for row in otopark:
        image += str(row) + "\n"
    return image


#def yer_bul(otopark):

#def arac_ekle(otopark, n):

main() 