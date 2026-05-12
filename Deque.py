# Boş bir liste oluşturuyoruz, bu bizim Deque'imiz olacak
kuyruk = []

def one_ekle(eleman):
    # insert(0, ...) listenin en başına eleman ekler
    kuyruk.insert(0, eleman)
    print(f"{eleman} başa eklendi.")

def sona_ekle(eleman):
    # append listenin en sonuna eleman ekler
    kuyruk.append(eleman)
    print(f"{eleman} sona eklendi.")

def bastan_sil():
    if len(kuyruk) > 0:
        silinen = kuyruk.pop(0)
        print(f"Baştan {silinen} silindi.")
        return silinen
    else:
        print("Hata: Kuyruk boş, silinecek eleman yok!")

def sondan_sil():
    if len(kuyruk) > 0:
        silinen = kuyruk.pop()
        print(f"Sondan {silinen} silindi.")
        return silinen
    else:
        print("Hata: Kuyruk boş!")

def yazdir():
    print("Kuyruğun şu anki hali:", kuyruk)

# --- Test Alanı ---

# Eleman ekleyelim
one_ekle(10)
one_ekle(20)
sona_ekle(30)
yazdir() # Çıktı: [20, 10, 30]

# Eleman silelim
bastan_sil()
sondan_sil()
yazdir() # Çıktı: [10]

# Boşken silmeye çalışalım (Hata kontrolü için)
bastan_sil()
bastan_sil()
