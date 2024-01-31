ilanlar = { }

while True :

    print("----------\n-İlan Eklemek: 1\n-İlan Çıkartmak: 2\n-Çıkış: 3")
    islem_numarasi = int(input("Yapmak istediğiniz işlemi seçin: "))

    if islem_numarasi == 1 :

        ad = input("İlan Adı Girin: ")

        if ad in ilanlar.keys() :
            print("Bu adlı bir ilan zaten var.")
            continue

        marka = input("Araba Markası Girin: ")
        model = input("Araba Modeli Girin: ")
        yil = input("Araba Yılını Girin: ")
        fiyat = input("Araba Fiyatını Girin: ")

        ozellikler = {}

        ozellikler["marka"] = marka
        ozellikler["model"] = model
        ozellikler["yıl"] = yil
        ozellikler["fiyat"] = fiyat
        ilanlar[ad] = ozellikler
        continue

    if islem_numarasi == 2 :
        silinecek_ad = input("Çıkaracağınız ilan adı şeçin: ")
        if silinecek_ad in ilanlar :
            ilanlar.pop(silinecek_ad)
        else :
            print("Böyle bir ilan yok.")
        continue

    if islem_numarasi == 3 :
        print("Çıkılıyor...")
        break

    else :
        print("Hatalı işlem numarası!")
        continue








