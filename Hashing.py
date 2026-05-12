class HashTable:
    def __init__(self, size=7):
        self.size = size
        # Her indeksi bos bir liste olarak baslatiyoruz (Chaining yontemi icin)
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        """
        Gelen anahtarin (string veya int) karakter toplamini alip 
        tablo boyutuna gore modunu alir.
        """
        if isinstance(key, str):
            ascii_sum = sum(ord(char) for char in key)
            return ascii_sum % self.size
        return key % self.size

    def insert(self, key, value):
        """Tabloya yeni eleman ekler veya var olani gunceller."""
        hash_index = self._hash_function(key)
        
        # Eger key zaten varsa degerini guncelle
        for pair in self.table[hash_index]:
            if pair[0] == key:
                pair[1] = value
                return
        
        # Key yoksa listenin sonuna ekle
        self.table[hash_index].append([key, value])
        print(f"'{key}' anahtari {hash_index} indeksine eklendi.")

    def search(self, key):
        """Key ile tabloda arama yapar."""
        hash_index = self._hash_function(key)
        for pair in self.table[hash_index]:
            if pair[0] == key:
                return pair[1]
        return None  # Bulunamazsa

    def delete(self, key):
        """Tablodan veri siler."""
        hash_index = self._hash_function(key)
        for i, pair in enumerate(self.table[hash_index]):
            if pair[0] == key:
                del self.table[hash_index][i]
                print(f"'{key}' basariyla silindi.")
                return True
        return False

    def display(self):
        """Tablonun guncel durumunu ekrana basar."""
        print("\n--- Hash Table Mevcut Durum ---")
        for i, slot in enumerate(self.table):
            print(f"Indeks {i}: {slot}")
        print("-------------------------------\n")

# --- Test Bolumu ---
if __name__ == "__main__":
    # Tablo boyutu 7 olan bir ornek olusturalim
    my_hash = HashTable(7)

    # Verilen dokumandaki ornekleri ekleyelim
    my_hash.insert("ab", "Grup 1")
    my_hash.insert("cd", "Grup 2")
    my_hash.insert("efg", "Grup 3")

    # Tabloyu goster
    my_hash.display()

    # Arama islemi
    print(f"Arama Sonucu (cd): {my_hash.search('cd')}")

    # Silme islemi
    my_hash.delete("ab")
    my_hash.display()
