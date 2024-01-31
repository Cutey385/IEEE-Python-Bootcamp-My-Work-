while (True):
    alphabets = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z']
    print("-----------")
    print("1-Şifreleme")
    print("2-Şifre Çözme")
    operation = int(input("İşlem Seçiniz: "))
    code = ""

    if operation == 1:
        text = input("Metin Girin: ")
        text = text.lower() 
        for i in range(len(text)):
            index = alphabets.index(text[i])
            if text[i] == 'z':
                code = code + alphabets[0]
            else:    
                code = code + alphabets[index + 1]    
        print(code)  

    elif operation == 2:
        text = input("Metin Girin: ") 
        text = text.lower()
        for i in range(len(text)):
            index = alphabets.index(text[i])
            if text[i] == 'a':
                code = code + 'z'  # alphabets[end]
            else:    
                code = code + alphabets[index - 1]    
        print(code)  

    # Break the loop with typing 3
    elif operation == 3:
        break   

    else:
       print("Hatalı işlem!")


