# 1. Bubble Sort (Baloncuk Siralamasi)
def bubble_sort(liste):
    n = len(liste)
    # Her elemani tek tek kontrol et
    for i in range(n):
        swapped = False # Degisim oldu mu kontrolu (optimizasyon icin)
        
        # Son i eleman zaten sirali oldugu icin n-i-1
        for j in range(0, n - i - 1):
            # Eger soldaki eleman sagdakinden buyukse yer degistir
            if liste[j] > liste[j + 1]:
                temp = liste[j]
                liste[j] = liste[j + 1]
                liste[j + 1] = temp
                swapped = True
        
        # Eger hic yer degisimi olmadiysa liste zaten siralidir, donguden cik
        if not swapped:
            break
    return liste

# 2. Insertion Sort (Eklemeli Siralama)
def insertion_sort(liste):
    # Birinci eleman sirali kabul edilir, 1. indexten baslanir
    for i in range(1, len(liste)):
        anahtar = liste[i] # Secilen eleman
        j = i - 1
        
        # Anahtar elemani kendinden oncekilerle karsilastir
        # Kendinden buyuk olanlari saga kaydir
        while j >= 0 and anahtar < liste[j]:
            liste[j + 1] = liste[j]
            j -= 1
        
        # Dogru bosluga anahtari yerlestir
        liste[j + 1] = anahtar
    return liste

# Test kismi
if __name__ == "__main__":
    # Bubble sort testi
    sayilar1 = [64, 34, 25, 12, 22, 11, 90]
    print("Orijinal Liste 1:", sayilar1)
    sirali_bubble = bubble_sort(sayilar1)
    print("Bubble Sort Sonucu:", sirali_bubble)
    
    print("-" * 30)
    
    # Insertion sort testi
    sayilar2 = [12, 11, 13, 5, 6]
    print("Orijinal Liste 2:", sayilar2)
    sirali_insertion = insertion_sort(sayilar2)
    print("Insertion Sort Sonucu:", sirali_insertion)
