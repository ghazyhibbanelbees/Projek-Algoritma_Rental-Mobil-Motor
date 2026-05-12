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

#biar password tidak terlihat
import getpass
import os # Untuk mengecek keberadaan file history
from datetime import datetime # Untuk fitur cek tanggal otomatis


#class node utama
class Node:
    def __init__(self, id, nama, jenis, harga, status="Ready"):
        self.id = id
        self.nama = nama
        self.status = status
        self.jenis = jenis
        self.harga = harga
        self.next = None

# ========================== STACK ==========================
class Stack:
    def __init__(self):
        self.data = []

    # menambahkan data ke atas stack
    def push(self, item):
        self.data.append(item)

    # mengambil data paling atas
    def pop(self):
        if not self.is_empty():
            return self.data.pop()

    # cek stack kosong atau tidak
    def is_empty(self):
        return len(self.data) == 0

    # menampilkan isi stack
    def tampilkan(self):
        if self.is_empty():
            print("Belum ada riwayat transaksi.")
            return

        print("\n" + "="*15 + " HISTORY SEWA (STACK) " + "="*15)
        print(f"{'Tanggal':<20} | {'Penyewa':<10} | {'Kendaraan':<15} | {'Biaya':<10}")
        print("-" * 65)

        # tampilkan dari transaksi terbaru
        for item in reversed(self.data):
            print(f"{item[0]:<20} | {item[1]:<10} | {item[2]:<15} | {item[3]:<10}")

    def tampilkan_history_user(self, username):
        #kalau kosong
        if self.is_empty():
            print("Belum ada riwayat transaksi.")
            return

        print("\n" + "="*25 + " HISTORY SEWA " + "="*25)
        print(f"{'Tanggal':<20} | {'Penyewa':<10} | {'Kendaraan':<15} | {'Biaya':<10}")
        print("-" * 65)

        # tampilkan dari transaksi terbaru
        for item in reversed(self.data):

            #item[1] = nama penyewa
            if item[1] == username:
                print(f"{item[0]:<20} | {item[1]:<10} | {item[2]:<15} | {item[3]:<10}")

# ========================== QUEUE (ANTREAN) ==========================
# node khusus untuk antrean
class NodeAntrean:
    def __init__(self, nama_user, id_kendaraan):
        self.nama_user = nama_user
        self.id_kendaraan = id_kendaraan
        self.next = None

# class queue untuk mengelola antrean
class QueueAntrean:
    def __init__(self):
        self.front = None
        self.rear = None

    # fungsi masuk antrean (enqueue)
    def enqueue(self, nama_user, id_kendaraan):
        # nodeA = node antrean baru
        nodeA = NodeAntrean(nama_user, id_kendaraan)
        # kalau antrean kosong
        if self.rear is None:
            self.front = self.rear = nodeA
            return
        # kalau tidak kosong, tambahkan di belakang
        self.rear.next = nodeA
        self.rear = nodeA

    # fungsi tampilkan antrean
    def tampilkan_antrean(self):
        # cegah error kalau antrean kosong
        if self.front is None:
            print("Antrean saat ini kosong.")
            return
        
        print("\n" + "="*15 + " DAFTAR ANTREAN (QUEUE) " + "="*15)
        current = self.front
        no = 1
        # looping semua antrean
        while current:
            print(f"{no}. User: {current.nama_user} mengantre ID: {current.id_kendaraan}")
            current = current.next
            no += 1


#class linked list
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

#==========================CRUD==============================

    # fungsi cek id duplicate
    def cek_id(self, id_baru):
        current = self.head
        # looping untuk mencari id yang sama
        while current:
            if current.id.upper() == id_baru.upper():
                return True # id ketemu
            current = current.next
        return False # id aman


    def tambah_kendaraan(self, id, nama, jenis, harga, status="Ready"):
        # validasi id duplicate
        if self.cek_id(id):
            print(f"Gagal! ID {id} sudah ada dalam sistem.")
            return False

        #nodeK = node kendaraan baru
        nodeK = Node(id, nama, jenis, harga, status)

        #kalau data masih kosong, node baru jadi head sekaligus tail
        if self.head is None:
            self.head = nodeK
            self.tail = nodeK

        #kalau tidak kosong
        else:
            #sisipkan nodeK ke ujung list, sebelah kanan tail
            self.tail.next = nodeK
            #jadikan nodeK menjadi tail baru
            self.tail = nodeK
        return True

    #fungsi tampilkan
    def tampilkan(self):
        current = self.head

        #cegah error kalau selfhead kosong/linkedlist kosong
        if self.head is None:
            print("Maaf, data masih kosong.")
            return
        
        #head table
        print(f"{'ID':<5} | {'Nama':<15} | {'Jenis':<10} | {'Harga':<10} | {'Status':<10}")
        print("-" * 60)

        #looping sampai ujung linked list
        while current is not None:

            #print semua data
            print(f"{current.id:<5} | {current.nama:<15} | {current.jenis:<10} | {current.harga:<10} | {current.status:<10}")
            current = current.next



    #Fungsi Update berdasarkan id
    def ubah_kendaraan(self, id):
        current = self.head

        #looping sampai ujung linked list
        while current is not None:

            #kalau id yang dicari sudah match
            if current.id.upper() == id.upper():

                #mmasukkan data baru
                print("Data ditemukan, masukkan data baru:")
                current.nama = input("Nama baru: ")
                current.jenis = input("Jenis baru: ")

                #try except untuk mencegah error kalau user input selain integer
                try:
                    current.harga = int(input("Harga baru: "))
                    #valueerror == salah data input
                except ValueError:
                    print("Harga harus angka!")
                    return
                current.status = input("Status baru (Ready/Dipakai): ")
                print("Data berhasil diubah!")
                return
            current = current.next

        print("ID tidak ditemukan!")


    #fungsi delete
    def hapus_kendaraan(self, id):
        current = self.head
        #variabel previous/sebelum
        prev = None

        #looping sampai ujung linked list
        while current is not None:

            #data sudah match
            if current.id.upper() == id.upper():

                #kalau ketemu di data pertama
                if prev is None:
                    #head pindah ke node kedua
                    self.head = current.next

                    #kalau node yang dihapus juga sebagai tail(berarti hanya ada 1 data di list)
                    if current == self.tail:
                        #list jadi kosong
                        self.tail = None
                else:
                    #hubungkan prev dengan current.next, contoh = 3->1->2 jadi 3->2
                    prev.next = current.next
                    
                    #kalau data adalah teil
                    if current == self.tail:
                        #tail mundur satu
                        self.tail = prev

                print("Kendaraan berhasil dihapus!")
                return
            

            #jadikan variabel prev sebagai current
            prev = current
            #current lanjut ke data selanjutnya
            current = current.next
        print("ID tidak ditemukan!")

#==========================SEARCHING AND SORTING==============================


    #bubble sort
    def sort_by_name(self):
        # kalau list kosong atau hanya 1 data, tidak perlu diurutkan
        if not self.head or not self.head.next:
            return
    
        swapped = True  # penanda apakah terjadi pertukaran data
        while swapped:
            swapped = False  # reset setiap iterasi
            current = self.head  # mulai dari head
        
            # loop sampai node terakhir
            while current.next:
            
                # bandingkan nama (pakai lower biar tidak sensitif huruf besar/kecil)
                if current.nama.lower() > current.next.nama.lower():
                
                    # tukar semua isi data antar node (bukan node-nya)
                    current.id, current.next.id = current.next.id, current.id
                    current.nama, current.next.nama = current.next.nama, current.nama
                    current.jenis, current.next.jenis = current.next.jenis, current.jenis
                    current.harga, current.next.harga = current.next.harga, current.harga
                    current.status, current.next.status = current.next.status, current.status
                
                    swapped = True  # tandai bahwa ada pertukaran
            
                # lanjut ke node berikutnya
                current = current.next
    
        print("Data berhasil diurutkan berdasarkan Nama (A-Z).")

    def cari_kendaraan(self, keyword):
        current = self.head  # mulai dari head linked list
        hasil = []  # list untuk menyimpan hasil pencarian

        # looping semua node
        while current:
            # cek apakah keyword ada di nama atau status (tidak sensitif huruf besar/kecil)
            if keyword.lower() in current.nama.lower() or keyword.lower() in current.status.lower():
                hasil.append(current)  # simpan node yang cocok
        
            current = current.next  # lanjut ke node berikutnya
    
        # jika ada hasil ditemukan
        if hasil:
            print(f"\n--- Hasil Pencarian '{keyword}' ---")
        
            # tampilkan semua hasil
            for node in hasil:
                print(f"ID: {node.id} | Nama: {node.nama} | Status: {node.status}")
                print()  # baris kosong biar rapi
        else:
            # jika tidak ada yang cocok
            print("Data tidak ditemukan.")


#==========================FILE HANDLING==============================

    def load_file(self, filename="dataKendaraan.txt"):
        import os  # import untuk cek file
    
        # cek apakah file ada atau tidak
        if not os.path.exists(filename):
            return  # kalau tidak ada, langsung keluar
    
        # buka file dalam mode read
        with open(filename, "r") as file:
            # baca file per baris
            for line in file:
            
                # hapus enter lalu pisahkan berdasarkan "|"
                data = line.strip().split("|")
            
                # pastikan jumlah data sesuai (5 kolom)
                if len(data) == 5:
                
                    # tambahkan ke linked list
                    # Menggunakan cara manual agar id dari file tidak kena validasi duplicate
                    nodeK = Node(data[0], data[1], data[2], int(data[3]), data[4])
                    if self.head is None:
                        self.head = nodeK
                        self.tail = nodeK
                    else:
                        self.tail.next = nodeK
                        self.tail = nodeK


    def simpan_file(self, filename="dataKendaraan.txt"):
        current = self.head  # mulai dari node pertama (head)
    
        # buka file dalam mode write (menimpa isi lama)
        with open(filename, "w") as file:
            # looping semua node
            while current is not None:
                # tulis data ke file dengan format dipisah "|"
                file.write(f"{current.id}|{current.nama}|{current.jenis}|{current.harga}|{current.status}\n")
            
                current = current.next  # pindah ke node berikutnya

#==========================FITUR SEWA & HISTORY==============================

    # Fungsi untuk melakukan transaksi sewa
    def sewa_kendaraan(self, id_cari, nama_penyewa, history, antrean):
        current = self.head

        while current:
            if current.id.upper() == id_cari.upper():

                if current.status.lower() == "ready":
                    current.status = "Dipakai"

                    tgl_sewa = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

                    # masukkan ke stack
                    history.push([
                        tgl_sewa,
                        nama_penyewa,
                        current.nama,
                        current.harga
                    ])

                    print(f"Berhasil menyewa {current.nama}!")
                    return True

                else:
                    # fitur antrean jika mobil sedang dipakai
                    print(f"Kendaraan {current.nama} sedang tidak tersedia (Dipakai).")
                    pilih_antrean = input("Ingin masuk antrean? (y/n): ")
                    if pilih_antrean.lower() == 'y':
                        antrean.enqueue(nama_penyewa, current.id)
                        print("Anda berhasil masuk antrean.")
                    return False

            current = current.next

        print("ID tidak ditemukan!")
        return False

    # Fungsi untuk menampilkan riwayat transaksi yang tersimpan di file
    def tampilkan_history(self):
        # Cek apakah file riwayat ada menggunakan library os
        if not os.path.exists("riwayatSewa.txt"):
            print("Belum ada riwayat transaksi.")
            return

        print("\n" + "="*15 + " HISTORY SEWA " + "="*15)
        print(f"{'Tanggal':<20} | {'Penyewa':<10} | {'Kendaraan':<15} | {'Biaya':<10}")
        print("-" * 65)
        
        # Baca file riwayat per baris
        with open("riwayatSewa.txt", "r") as file:
            for line in file:
                data = line.strip().split("|")
                if len(data) == 4:
                    print(f"{data[0]:<20} | {data[1]:<10} | {data[2]:<15} | {data[3]:<10}")


#========================Fitur Login===================
#cegah username yang duplikat
def username_duplikat(username):
    try:
        with open("dataAkun.txt", "r") as file:
            #cek satu persatu line
            for line in file:
                #jadikan data per line data individual masing masing, dan jadi list
                data = line.strip().split("|")
                #cek apakah username sudah ada di file
                if username==data[0]:
                    return True
                
    except:
        pass
    return False

def register():
    print("\n" + "="*20 + " Register " + "="*20)
    username = input("Username: ")
    password = input("Password: ")
    
    #kalau return true
    if username_duplikat(username):
        print("Username sudah terpakai!")
        return
    
    #buka file untuk append
    with open("dataAkun.txt", "a") as file:
        file.write(f"{username}|{password}|user\n")
    
    print("Akun selesai dibuat!")

def login():
    print("\n" + "="*20 + " Login " + "="*20)
    #Input username dan password
    username = input("Username: ")
    password = input("Password: ")

    try:
        #read file akun
        with open("dataAkun.txt", "r") as file:
            #cek setiap line di file
            for line in file:
                #pisahkan data di line berdasarkan "|" dan dijadikan list
                data = line.strip().split("|")
                #kalau username dan password match dengan yang ada di file, login berhasil
                if username == data[0] and password == data[1]:
                    print("Login Berhasil")
                    return data[0], data[2] # Mengembalikan username dan role
    
    #cegah error file tidak ada
    except FileNotFoundError:
        print("File akun belum ada!")

    print("Username atau password salah.")
    return None, None



def main():
    ll = LinkedList()
    ll.load_file()
    history = Stack()
    antrean = QueueAntrean() # inisialisasi class queue

    role = None
    user_aktif = None

    while role is None:
        print("\n" + "="*20 + " Rental Mobil dan Motor Babeh Ipul " + "="*20)
        print("1. Login")
        print("2. Register")
        print("0. Keluar")

        pilih=input("Pilih menu(1-2): ")

        if pilih == "1":
            user_aktif, role = login()
        elif pilih == "2":
            register()
        elif pilih == "0":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")
    
    if role == "admin":
        while True:
            # ll.tampilkan() # Dihapus dari loop agar menu lebih rapi
            print()
            print("\n" + "="*20 + " Rental Mobil dan Motor Babeh Ipul " + "="*20)
            print(f"User: {user_aktif} | Role: {role}")
            print("-" * 40)
            print("1. Tambah Kendaraan")
            print("2. Tampilkan Daftar Kendaraan")
            print("3. Ubah Data Kendaraan")
            print("4. Hapus Data Kendaraan")
            print("5. Urutkan Kendaraan (A-Z)")
            print("6. Cari Kendaraan (Nama/Status)")
            print("7. Sewa Kendaraan") 
            print("8. Riwayat Sewa & Cek Tanggal") 
            print("9. Lihat Antrean (Queue)") # Menu baru antrean
            print("0. Keluar")
            
            pilih = input("Pilih Menu (0-9): ")
            
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
                # memanggil fungsi tambah dengan validasi id duplicate
                if ll.tambah_kendaraan(id, nama, jenis, harga):
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

            elif pilih == "7": # Eksekusi Fitur Sewa
                ll.tampilkan()
                id_sewa = input("Masukkan ID kendaraan yang ingin disewa: ")
                if ll.sewa_kendaraan(id_sewa, user_aktif, history, antrean):
                    ll.simpan_file() # Update status kendaraan ke file
                
            elif pilih == "8": # Eksekusi Fitur History & Tanggal
                # Fitur cek tanggal hari ini
                print(f"\nTanggal Hari Ini: {datetime.now().strftime('%d %B %Y')}")
                history.tampilkan()

            elif pilih == "9": # Eksekusi Tampilkan Queue
                antrean.tampilkan_antrean()
                
            elif pilih == "0":
                print("Terima kasih!")
                break
            else:
                print("Pilihan tidak valid.")

    elif role == "user":
        while True:
            # ll.tampilkan() # Dihapus dari loop agar menu lebih rapi
            print()
            print("\n" + "="*20 + " Rental Mobil dan Motor Babeh Ipul " + "="*20)
            print(f"User: {user_aktif} | Role: {role}")
            print("-" * 40)
            print("1. Tampilkan Daftar Kendaraan")
            print("2. Urutkan Kendaraan (A-Z)")
            print("3. Cari Kendaraan (Nama/Status)")
            print("4. Sewa Kendaraan (Fitur Antrean)") 
            print("5. Riwayat Sewa Saya") 
            print("6. Lihat Antrean") # Menu antrean untuk user
            print("0. Keluar")
            
            pilih = input("Pilih Menu (0-6): ")
                
            if pilih == "1":
                print("\n======== Daftar Kendaraan ========")
                ll.tampilkan()
                
            elif pilih == "2":
                ll.sort_by_name()
                ll.tampilkan()
                ll.simpan_file() 
                
            elif pilih == "3":
                keyword = input("Masukkan nama atau status yang dicari: ")
                ll.cari_kendaraan(keyword)

            elif pilih == "4": # Eksekusi Fitur Sewa
                ll.tampilkan()
                id_sewa = input("Masukkan ID kendaraan yang ingin disewa: ")
                if ll.sewa_kendaraan(id_sewa, user_aktif, history, antrean):
                    ll.simpan_file() # Update status kendaraan ke file
                
            elif pilih == "5": # Eksekusi Fitur History & Tanggal
                # Fitur cek tanggal hari ini
                print(f"\nTanggal Hari Ini: {datetime.now().strftime('%d %B %Y')}")
                history.tampilkan_history_user(user_aktif)

            elif pilih == "6": # Eksekusi Tampilkan Queue
                antrean.tampilkan_antrean()
                
            elif pilih == "0":
                print("Terima kasih!")
                break
            else:
                print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
