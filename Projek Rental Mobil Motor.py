# ==============================================
# Kelompok 23
# Nama:
# Adrian Hermawan - J0403251044
# Ghazyhibban Kumayl Elbees - J0403251
# Kelas : B1
# ==============================================

# ==============================================
# Projek Matakuliah Algoritma dan Struktur Data:
# Rental Mobil dan Motor
# ==============================================

class Node:
    def __init__(self, id, nama, jenis, harga, status = "Ready"):
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
    
    def tampilkan(self):
        current = self.head
        
        if self.head is None:
            print("Maaf, data masih kosong.")
            return


        while current is not None:
            print(f"{current.id}. Nama Mobil: {current.nama}, Jenis:")
            
            current = current.next
            
    def tambah_kendaraan(self, id, nama, jenis, harga, status = "Ready"):
        nodeK = Node(id, nama, jenis, harga, status)
        
        if self.head is None:
            self.head = nodeK
            self.tail = nodeK
        else:
            self.tail.next = nodeK
            self.tail = nodeK
        
    def ubah_kendaraan(self, id):
        current = self.head

        #loop dari head ke tail
        while current is not None:
            #kalau ketemu idnya
            if current.id == id:
                print("Data ditemukan, masukkan data baru:")

                #ganti data baru
                current.nama = input("Nama baru: ")
                current.jenis = input("Jenis baru: ")

                try:
                    current.harga = int(input("Harga baru: "))
                except:
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
                # kasus: hapus head
                if prev is None:
                    self.head = current.next
                    if current == self.tail:  # kalau cuma 1 node
                        self.tail = None
                else:
                    prev.next = current.next
                    if current == self.tail:  # hapus tail
                        self.tail = prev

                print("Kendaraan berhasil dihapus!")
                return
            
            prev = current
            current = current.next

        print("ID tidak ditemukan!")
        
def main():
    ll = LinkedList()
    ll.tambah_kendaraan("A1", "Pajero", "SUV", 1000000)
    ll.tambah_kendaraan("A2", "Lamborghini", "Sportcar", 2000000)
    ll.tambah_kendaraan("A3", "Xpander", "SUV", 900000)
    ll.tambah_kendaraan("A4","Avanza", "Bensin", 500000)
    ll.tampilkan()
    
    while True:
        print("\n===================== Rental Mobil dan Motor Babeh Ipul =====================")
        print("1. Tambah Kendaraan")
        print("2. Tampilkan Daftar Kendaraan")
        print("3. Ubah Data Kendaraan")
        print("4. Hapus Data Kendaraan")
        print("0. Keluar")
        
        pilih = input("Pilih Menu (1-4): ")
        if pilih == "1":
            print("\n========Tambah Kendaraan========")

            id = input("Masukkan id: ")
            nama = input("Masukkan Nama Kendaraan: ")
            jenis = input("Masukkan jenis (Mobil/Motor): ")

            try:
                harga = int(input("Masukkan harga sewa: "))
            except:
                print("Harga harus angka!")
                continue

            ll.tambah_kendaraan(id,nama,jenis,harga)
            print("Kendaraan berhasil ditambahkan!")
        elif pilih == "2":
            ll.tampilkan()
        elif pilih == "3":
            print("\n======== Ubah Data Kendaraan ========")
            id = input("Masukkan ID kendaraan yang ingin diubah: ")
            ll.ubah_kendaraan(id)
        elif pilih == "4":
            print("\n======== Hapus Kendaraan ========")
            id = input("Masukkan ID kendaraan yang ingin dihapus: ")
            ll.hapus_kendaraan(id)
        elif pilih == "0":
            break

if __name__ == "__main__":
        main()