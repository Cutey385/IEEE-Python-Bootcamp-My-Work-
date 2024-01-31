ana_para = int(input("Ana para: "))
vade = int(input("Vade: "))
yillik_faiz_orani = int(input("Yıllık faiz oranı: "))

aylik_faiz_orani = yillik_faiz_orani / 12
yuzde_toplam_faiz = round(((aylik_faiz_orani * vade) / 100), 1)
faiz_getirisi = round(yuzde_toplam_faiz * ana_para)

print(f"{vade} ay sonunda, yıllık %{yillik_faiz_orani} faiz oranı ile {ana_para}TL ana paradan {faiz_getirisi}TL faiz geliri elde edilecektir.")