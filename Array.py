# Tek boyutlu bir dizi tanimlayalim (Ogrenci notlari örnegi)
notlar = [65, 70, 95, 40, 80, 55]

# Dizinin ilk halini yazdirma
print("Dizi elemanlari:", notlar)

# Index kullanarak eleman degistirme (Update)
notlar[3] = 50  # 40 olan notu 50 ile guncelledik
print("Guncel notlar:", notlar)

# Dizinin sonuna eleman ekleme (Dynamic array gibi)
notlar.append(100)

# Bir dongu yardimiyla diziyi donelim ve 60'tan buyuk olanlari sayalim
basarili_sayisi = 0
for n in notlar:
    if n >= 60:
        basarili_sayisi += 1

print("Gecen ogrenci sayisi:", basarili_sayisi)

# ---------------------------------------------------------
# Cok boyutlu dizi (Matrix) ornegi
# 3x3 luk bir matris olusturalim

matris = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\nMatris Yapisi:")
for satir in matris:
    print(satir)

# Matrisin icinden spesifik bir elemani alma
# Ornegin 2. satirin 3. elemani (Indexler 0'dan baslar)
eleman = matris[1][2] 
print("\nMatrisin [1][2] indexindeki eleman:", eleman)

# Matrisin tum elemanlarini toplama
toplam = 0
for i in range(len(matris)):
    for j in range(len(matris[i])):
        toplam += matris[i][j]

print("Matris elemanlarinin toplami:", toplam)
