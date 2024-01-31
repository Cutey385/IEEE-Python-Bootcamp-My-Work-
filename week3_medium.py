def add(sayi1, sayi2) :
    return sayi1 + sayi2

def subtract(sayi1 , sayi2) :
    return sayi1 - sayi2

def multiply(sayi1 , sayi2) :
    return sayi1 * sayi2

def divide(sayi1, sayi2):
    if sayi2 != 0:
        return sayi1 / sayi2
    else:
        print("0'a bölme işlemi yapılamaz!")
        return None

def get_user_input():
    while True :
        try:
            sayi1 = float(input("İlk sayı: "))
            sayi2 = float(input("İkinci sayı: "))
            return sayi1, sayi2
        except ValueError:
            print("Geçersiz sayı girişi!")

def calculator() :
    while True :
        print("İşlem seçin:\n1. Toplama (+)\n2. Çıkarma (-)\n3. Çarpma (*)\n4. Bölme (/)\n5. Çıkış")
        operation = int(input("İşlem seçiniz:"))

        if operation == 5 :
            print("Çıkış yapılıyor...")
            break

        if operation in {1, 2, 3, 4} :
            sayi1 , sayi2 = get_user_input()

            if operation == 1 :
                sonuc = add(sayi1 , sayi2)
            elif operation == 2 :
                sonuc = subtract(sayi1, sayi2)
            elif operation == 3 :
                sonuc = multiply(sayi1, sayi2)
            elif operation == 4 :
                sonuc = divide(sayi1, sayi2)

            if sonuc != None :
                print(f"Sonuç = {sonuc}")

        else:
            print("Hatalı işlem seçimi yaptınız.")


calculator()
