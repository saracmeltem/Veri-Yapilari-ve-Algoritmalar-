class Node:
    def __init__(self, veri):
        self.veri = veri
        self.sonraki = None # baslangicta bos

class BagliListe:
    def __init__(self):
        self.bas = None # head dugumu

    # Listenin basina eleman ekleme
    def basa_ekle(self, yeni_veri):
        yeni_dugum = Node(yeni_veri)
        yeni_dugum.sonraki = self.bas
        self.bas = yeni_dugum
        print(str(yeni_veri) + " basa eklendi.")

    # Listenin sonuna eleman ekleme
    def sona_ekle(self, veri):
        yeni_dugum = Node(veri)
        if self.bas is None:
            self.bas = yeni_dugum
            return
        
        gecici = self.bas
        while gecici.sonraki: # sona kadar git
            gecici = gecici.sonraki
        
        gecici.sonraki = yeni_dugum
        print(str(veri) + " sona eklendi.")

    # Listeyi ekrana yazdirma fonksiyonu
    def listele(self):
        print("\n--- Guncel Liste ---")
        temp = self.bas
        if temp is None:
            print("Liste su an bos!")
            return

        while temp:
            print(temp.veri, end=" -> ")
            temp = temp.sonraki
        print("None") # listenin sonu

    # Eleman silme (veriye gore)
    def eleman_sil(self, silinecek):
        temp = self.bas
        onceki = None

        # Eger ilk eleman silinecekse
        if temp is not None and temp.veri == silinecek:
            self.bas = temp.sonraki
            temp = None
            return

        # Silinecek elemani ara
        while temp is not None:
            if temp.veri == silinecek:
                break
            onceki = temp
            temp = temp.sonraki

        if temp == None:
            print("Eleman bulunamadi.")
            return

        onceki.sonraki = temp.sonraki
        temp = None

    # Listenin uzunlugunu bulma
    def uzunluk(self):
        sayac = 0
        gecici = self.bas
        while gecici:
            sayac += 1
            gecici = gecici.sonraki
        return sayac

    # Listeyi tersine cevirme (Odevdeki ekstra puan kismi)
    def ters_cevir(self):
        onceki = None
        suanki = self.bas
        while suanki:
            sonraki_yedek = suanki.sonraki
            suanki.sonraki = onceki
            onceki = suanki
            suanki = sonraki_yedek
        self.bas = onceki
        print("Liste tersine cevrildi.")

# --- Test Bolumu ---
if __name__ == "__main__":
    liste = BagliListe()
    
    liste.basa_ekle(10)
    liste.basa_ekle(20)
    liste.sona_ekle(30)
    liste.sona_ekle(40)
    
    liste.listele()
    
    print("Liste boyutu:", liste.uzunluk())
    
    liste.eleman_sil(20)
    print("20 siliniyor...")
    liste.listele()
    
    liste.ters_cevir()
    liste.listele()
