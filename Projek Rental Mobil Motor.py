# ==============================================
# Kelompok 22
# Nama:
# Adrian Hermawan - J0403251044
# Ghazyhibban Kumayl Elbees - J0403251136
# Kelas : B1
# ==============================================

# ==============================================
# Projek Matakuliah Algoritma dan Struktur Data:
# Rental Mobil dan Motor
# ==============================================

class Node:
    def __init__(self, id, nama, jenis, harga, status="Ready"):
        self.id = id
        self.nama = nama
        self.status = status
        self.jenis = jenis
        self.harga = harga
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah_kendaraan(self, id, nama, jenis, harga, status="Ready"):
        nodeK = Node(id, nama, jenis, harga, status)
        if self.head is None:
            self.head = nodeK
            self.tail = nodeK
        else:
            self.tail.next = nodeK
            self.tail = nodeK

    def tampilkan(self):
        current = self.head
        if self.head is None:
            print("Maaf, data masih kosong.")
            return
        
        print(f"{'ID':<5} | {'Nama':<15} | {'Jenis':<10} | {'Harga':<10} | {'Status':<10}")
        print("-" * 60)
        while current is not None:
            print(f"{current.id:<5} | {current.nama:<15} | {current.jenis:<10} | {current.harga:<10} | {current.status:<10}")
            current = current.next

    def ubah_kendaraan(self, id):
        current = self.head
        while current is not None:
            if current.id == id:
                print("Data ditemukan, masukkan data baru:")
                current.nama = input("Nama baru: ")
                current.jenis = input("Jenis baru: ")
                try:
                    current.harga = int(input("Harga baru: "))
                except ValueError:
                    print("Harga harus angka!")
                    return
                current.status = input("Status baru (Ready/Dipakai): ")
                print("Data berhasil diubah!")
                return
            current = current.next
        print("ID tidak ditemukan!")

    def hapus_kendaraan(self, id):
        current = self.head
        prev = None
        while current is not None:
            if current.id == id:
                if prev is None:
                    self.head = current.next
                    if current == self.tail:
                        self.tail = None
                else:
                    prev.next = current.next
                    if current == self.tail:
                        self.tail = prev
                print("Kendaraan berhasil dihapus!")
                return
            prev = current
            current = current.next
        print("ID tidak ditemukan!")

    def sort_by_name(self):
        if not self.head or not self.head.next:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if current.nama.lower() > current.next.nama.lower():
                    current.id, current.next.id = current.next.id, current.id
                    current.nama, current.next.nama = current.next.nama, current.nama
                    current.jenis, current.next.jenis = current.next.jenis, current.jenis
                    current.harga, current.next.harga = current.next.harga, current.harga
                    current.status, current.next.status = current.next.status, current.status
                    swapped = True
                current = current.next
        print("Data berhasil diurutkan berdasarkan Nama (A-Z).")

    def cari_kendaraan(self, keyword):
        current = self.head
        hasil = []
        while current:
            if keyword.lower() in current.nama.lower() or keyword.lower() in current.status.lower():
                hasil.append(current)
            current = current.next
        
        if hasil:
            print(f"\n--- Hasil Pencarian '{keyword}' ---")
            for node in hasil:
                print(f"ID: {node.id} | Nama: {node.nama} | Status: {node.status}")
        else:
            print("Data tidak ditemukan.")

    def simpan_file(self, filename="dataKendaraan.txt"):
        current = self.head
        with open(filename, "w") as file:
            while current is not None:
                file.write(f"{current.id}|{current.nama}|{current.jenis}|{current.harga}|{current.status}\n")
                current = current.next

    def load_file(self, filename="dataKendaraan.txt"):
        if not os.path.exists(filename):
            return
        with open(filename, "r") as file:
            for line in file:
                data = line.strip().split("|")
                if len(data) == 5:
                    self.tambah_kendaraan(data[0], data[1], data[2], int(data[3]), data[4])

def main():
    ll = LinkedList()
    ll.load_file()
    
    while True:
        print("\n" + "="*20 + " Rental Mobil dan Motor Babeh Ipul " + "="*20)
        print("1. Tambah Kendaraan")
        print("2. Tampilkan Daftar Kendaraan")
        print("3. Ubah Data Kendaraan")
        print("4. Hapus Data Kendaraan")
        print("5. Urutkan Kendaraan (A-Z)")
        print("6. Cari Kendaraan (Nama/Status)")
        print("0. Keluar")
        
        pilih = input("Pilih Menu (0-6): ")
        
        if pilih == "1":
            print("\n======== Tambah Kendaraan ========")
            id = input("Masukkan ID: ")
            nama = input("Masukkan Nama Kendaraan: ")
            jenis = input("Masukkan Jenis (Mobil/Motor): ")
            try:
                harga = int(input("Masukkan Harga Sewa: "))
            except ValueError:
                print("Harga harus angka!")
                continue
            ll.tambah_kendaraan(id, nama, jenis, harga)
            ll.simpan_file()
            print("Kendaraan berhasil ditambahkan!")
            
        elif pilih == "2":
            print("\n======== Daftar Kendaraan ========")
            ll.tampilkan()
            
        elif pilih == "3":
            id = input("Masukkan ID kendaraan yang ingin diubah: ")
            ll.ubah_kendaraan(id)
            ll.simpan_file()
            
        elif pilih == "4":
            id = input("Masukkan ID kendaraan yang ingin dihapus: ")
            ll.hapus_kendaraan(id)
            ll.simpan_file()
            
        elif pilih == "5":
            ll.sort_by_name()
            ll.tampilkan()
            ll.simpan_file() 
            
        elif pilih == "6":
            keyword = input("Masukkan nama atau status yang dicari: ")
            ll.cari_kendaraan(keyword)
            
        elif pilih == "0":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
