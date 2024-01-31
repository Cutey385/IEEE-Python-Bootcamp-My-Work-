class Sekil:
    def __init__(self, kenar_sayisi):
        self.kenar_sayisi = kenar_sayisi

    def iç_açılar_toplamı(self):
        toplam = (self.kenar_sayisi - 2) * 180
        return toplam

    def bir_ic_aci(self):
       ic_aci = self.iç_açılar_toplamı()  / self.kenar_sayisi
       return ic_aci


