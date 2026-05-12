def iki_toplam_var_mi(liste, hedef):
    """
    Bu fonksiyon, sirali bir listede toplamlari 'hedef' degerine 
    esit olan iki sayi olup olmadigini kontrol eder.
    """
    
    # Listeyi garantiye almak icin siraliyoruz (Two pointers icin sart)
    # Eger hoca diziyi zaten sirali verirse burasi silinebilir
    liste.sort() 
    
    sol = 0                 # Listenin en basi
    sag = len(liste) - 1    # Listenin en sonu
    
    # Isaretciler birbirine carpana kadar devam et
    while sol < sag:
        su_anki_toplam = liste[sol] + liste[sag]
        
        if su_anki_toplam == hedef:
            # Hedefi bulduk!
            print(f"Bulundu: {liste[sol]} + {liste[sag]} = {hedef}")
            return True
        
        elif su_anki_toplam < hedef:
            # Toplam kucuk kaldi, degeri artirmak icin soldaki isaretciyi saga cek
            sol += 1
        else:
            # Toplam cok buyuk, azaltmak icin sagdaki isaretciyi sola cek
            sag -= 1
            
    # Hicbir sey bulamazsak False doner
    print("Maalesef hedef toplama ulasan ikili yok.")
    return False

# Test kismi
if __name__ == "__main__":
    sayilar = [0, -1, 2, -3, 1]
    hedef_sayi = -2
    
    print("Dizi:", sayilar)
    print("Hedef:", hedef_sayi)
    
    sonuc = iki_toplam_var_mi(sayilar, hedef_sayi)
    print("Sonuc:", sonuc)
