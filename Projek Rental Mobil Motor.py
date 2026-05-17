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

import os # Untuk mengecek keberadaan file history
from datetime import datetime, timedelta # Untuk fitur cek tanggal otomatis
 

#class node utama
class Node:

    def __init__(self, id, nama, jenis, harga, status="Ready", tanggal_kembali="-", penyewa_aktif="-"):
        self.id = id
        self.nama = nama
        self.status = status
        self.jenis = jenis
        self.harga = harga
        self.tanggal_kembali = tanggal_kembali
        
        # Fitur 14: Tambahan atribut penyewa aktif
        self.penyewa_aktif = penyewa_aktif
        
        self.next = None


# ========================== STACK (RIWAYAT) ===================================

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


    # simpan history ke file
    def simpan_history(self, item, filename="riwayatSewa.txt"):

        with open(filename, "a") as file:
            file.write(f"{item[0]}|{item[1]}|{item[2]}|{item[3]}\n")


    # load history dari file
    def load_history(self, filename="riwayatSewa.txt"):

        if not os.path.exists(filename):
            return

        with open(filename, "r") as file:
            for line in file:
                data = line.strip().split("|")

                if len(data) == 4:
                    self.push(data)


# ========================== QUEUE (ANTREAN) ===================================

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


    # fungsi keluar antrean (dequeue)
    def dequeue(self):

        # kalau antrean kosong
        if self.front is None:
            return None

        data_keluar = self.front

        # pindahkan front ke node berikutnya
        self.front = self.front.next

        # kalau antrean jadi kosong
        if self.front is None:
            self.rear = None

        return data_keluar


    def simpan_antrean(self, filename = "dataAntrean.txt"):

        current = self.front
        
        with open(filename,"w") as file:
            while current:
                file.write(f"{current.nama_user}|{current.id_kendaraan}\n")
                current = current.next


    def load_antrean(self, filename = "dataAntrean.txt"):

        if not os.path.exists(filename):
            return
        
        with open(filename, "r") as file:
            for line in file:

                data = line.strip().split("|")

                if len(data) == 2:
                    self.enqueue(data[0], data[1])


# ========================== LINKED LIST (DATA) ================================

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None


# ================================ CRUD ========================================

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
       print(f"{'ID':<5} | {'Nama':<15} | {'Jenis':<10} | {'Harga':<10} | {'Status':<10} | {'Penyewa':<12} | {'Kembali':<15}")
print("-" * 110)

        #looping sampai ujung linked list
        while current is not None:

            #print semua data
            print(f"{current.id:<5} | {current.nama:<15} | {current.jenis:<10} | {current.harga:<10} | {current.status:<10} | {current.penyewa_aktif:<12} | {current.tanggal_kembali:<15}")


    def tampilkan_khusus_sewa(self):

        current = self.head

        print(f"{'ID':<5} | {'Nama':<15} | {'Penyewa':<10} | {'Status':<10} | {'Kembali':<15}")
        print("-" * 70)

        while current:

            if current.status == "Dipakai" or current.status == "Telat":
                print(f"{current.id:<5} | {current.nama:<15} | {current.penyewa_aktif:<10} | {current.status:<10} | {current.tanggal_kembali:<15}")
            
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


#========================== SEARCHING AND SORTING ==============================


    #bubble sort berdasarkan Nama
    def sort_by_name_asc(self):

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
                    current.tanggal_kembali, current.next.tanggal_kembali = current.next.tanggal_kembali, current.tanggal_kembali
                    current.penyewa_aktif, current.next.penyewa_aktif = current.next.penyewa_aktif, current.penyewa_aktif
                
                    swapped = True  # tandai bahwa ada pertukaran
            
                # lanjut ke node berikutnya
                current = current.next
    
        print("Data berhasil diurutkan berdasarkan Nama (A-Z).")


    def sort_by_name_dsc(self):

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
                if current.nama.lower() < current.next.nama.lower():
                
                    # tukar semua isi data antar node (bukan node-nya)
                    current.id, current.next.id = current.next.id, current.id
                    current.nama, current.next.nama = current.next.nama, current.nama
                    current.jenis, current.next.jenis = current.next.jenis, current.jenis
                    current.harga, current.next.harga = current.next.harga, current.harga
                    current.status, current.next.status = current.next.status, current.status
                    current.tanggal_kembali, current.next.tanggal_kembali = current.next.tanggal_kembali, current.tanggal_kembali
                    current.penyewa_aktif, current.next.penyewa_aktif = current.next.penyewa_aktif, current.penyewa_aktif
                
                    swapped = True  # tandai bahwa ada pertukaran
            
                # lanjut ke node berikutnya
                current = current.next
    
        print("Data berhasil diurutkan berdasarkan Nama (Z-A).")


    def sort_by_price_asc(self):

        if not self.head or not self.head.next:
            return

        swapped = True

        while swapped:
            swapped = False
            current = self.head

            while current.next:

                if current.harga > current.next.harga:
                    # Tukar data
                    current.id, current.next.id = current.next.id, current.id
                    current.nama, current.next.nama = current.next.nama, current.nama
                    current.jenis, current.next.jenis = current.next.jenis, current.jenis
                    current.harga, current.next.harga = current.next.harga, current.harga
                    current.status, current.next.status = current.next.status, current.status
                    current.tanggal_kembali, current.next.tanggal_kembali = current.next.tanggal_kembali, current.tanggal_kembali
                    current.penyewa_aktif, current.next.penyewa_aktif = current.next.penyewa_aktif, current.penyewa_aktif
                    
                    swapped = True

                current = current.next

        print("Data berhasil diurutkan berdasarkan Harga.")


    def sort_by_price_dsc(self):

        if not self.head or not self.head.next:
            return

        swapped = True

        while swapped:
            swapped = False
            current = self.head

            while current.next:

                if current.harga < current.next.harga:
                    # Tukar data
                    current.id, current.next.id = current.next.id, current.id
                    current.nama, current.next.nama = current.next.nama, current.nama
                    current.jenis, current.next.jenis = current.next.jenis, current.jenis
                    current.harga, current.next.harga = current.next.harga, current.harga
                    current.status, current.next.status = current.next.status, current.status
                    current.tanggal_kembali, current.next.tanggal_kembali = current.next.tanggal_kembali, current.tanggal_kembali
                    current.penyewa_aktif, current.next.penyewa_aktif = current.next.penyewa_aktif, current.penyewa_aktif
                    
                    swapped = True

                current = current.next

        print("Data berhasil diurutkan berdasarkan Harga.")

    def sort_by_status(self):

        # kalau list kosong atau hanya 1 data
        if not self.head or not self.head.next:
            return

        swapped = True

        while swapped:
            swapped = False
            current = self.head

            while current.next:

                # prioritas:
                # Ready -> Dipakai -> Telat
                urutan_status = {
                    "Ready": 1,
                    "Dipakai": 2,
                    "Telat": 3
                }

                status_sekarang = urutan_status.get(current.status, 99)
                status_berikut = urutan_status.get(current.next.status, 99)

                # kalau urutan salah, tukar
                if status_sekarang > status_berikut:

                    # tukar semua data node
                    current.id, current.next.id = current.next.id, current.id
                    current.nama, current.next.nama = current.next.nama, current.nama
                    current.jenis, current.next.jenis = current.next.jenis, current.jenis
                    current.harga, current.next.harga = current.next.harga, current.harga
                    current.status, current.next.status = current.next.status, current.status
                    current.tanggal_kembali, current.next.tanggal_kembali = current.next.tanggal_kembali, current.tanggal_kembali
                    current.penyewa_aktif, current.next.penyewa_aktif = current.next.penyewa_aktif, current.penyewa_aktif

                    swapped = True

                current = current.next

        print("Data berhasil diurutkan berdasarkan status.")
    

    def cari_kendaraan_nama(self, keyword):

        current = self.head  # mulai dari head linked list
        hasil = []  # list untuk menyimpan hasil pencarian

        # looping semua node
        while current:

            # cek apakah keyword ada di nama (tidak sensitif huruf besar/kecil)
            if keyword.lower() in current.nama.lower() :
                hasil.append(current)  # simpan node yang cocok
        
            current = current.next  # lanjut ke node berikutnya
    
        # jika ada hasil ditemukan
        if hasil:
            print(f"\n--- Hasil Pencarian '{keyword}' ---")
        
            # tampilkan semua hasil
            for node in hasil:
                print(f"ID: {node.id} | Nama: {node.nama} | Jenis: {node.jenis} | Status: {node.status}")
                print()  # baris kosong biar rapi
        else:
            # jika tidak ada yang cocok
            print("Data tidak ditemukan.")

    def cari_kendaraan_status(self, keyword):

        current = self.head  # mulai dari head linked list
        hasil = []  # list untuk menyimpan hasil pencarian

        # looping semua node
        while current:

            # cek apakah keyword ada di nama (tidak sensitif huruf besar/kecil)
            if keyword.lower() in current.status.lower() :
                hasil.append(current)  # simpan node yang cocok
        
            current = current.next  # lanjut ke node berikutnya
    
        # jika ada hasil ditemukan
        if hasil:
            print(f"\n--- Hasil Pencarian '{keyword}' ---")
        
            # tampilkan semua hasil
            for node in hasil:
                print(f"ID: {node.id} | Nama: {node.nama} | Jenis: {node.jenis} | Status: {node.status}")
                print()  # baris kosong biar rapi
        else:
            # jika tidak ada yang cocok
            print("Data tidak ditemukan.")

    def cari_kendaraan_jenis(self, keyword):

        current = self.head  # mulai dari head linked list
        hasil = []  # list untuk menyimpan hasil pencarian

        # looping semua node
        while current:

            # cek apakah keyword ada di nama (tidak sensitif huruf besar/kecil)
            if keyword.lower() in current.jenis.lower() :
                hasil.append(current)  # simpan node yang cocok
        
            current = current.next  # lanjut ke node berikutnya
    
        # jika ada hasil ditemukan
        if hasil:
            print(f"\n--- Hasil Pencarian '{keyword}' ---")
        
            # tampilkan semua hasil
            for node in hasil:
                print(f"ID: {node.id} | Nama: {node.nama} | Jenis: {node.jenis} | Status: {node.status}")
                print()  # baris kosong biar rapi
        else:
            # jika tidak ada yang cocok
            print("Data tidak ditemukan.")


#========================== FILE HANDLING ==============================

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
            
                # pastikan jumlah data sesuai (6 kolom)
                if len(data) == 7:
                
                    # tambahkan ke linked list
                    # Menggunakan cara manual agar id dari file tidak kena validasi duplicate
                    nodeK = Node(data[0], data[1], data[2], int(data[3]), data[4], data[5], data[6])

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
                file.write(f"{current.id}|{current.nama}|{current.jenis}|{current.harga}|{current.status}|{current.tanggal_kembali}|{current.penyewa_aktif}\n")
            
                current = current.next  # pindah ke node berikutnya


#========================== FITUR SEWA & HISTORY ==============================

    # Fungsi untuk melakukan transaksi sewa
    def sewa_kendaraan(self, id_cari, nama_penyewa, history, antrean):

        current = self.head

        while current:

            if current.id.upper() == id_cari.upper():

                if current.status == "Dipakai" and current.penyewa_aktif == nama_penyewa:
                    print("\nAnda sedang menyewa unit ini.")
                    ext = input("Perpanjang sewa? (y/n): ")

                    if ext.lower() == 'y':
                        hari = int(input("Tambah berapa hari?: "))
                        tgl_lama = datetime.strptime(current.tanggal_kembali, "%d-%m-%Y")
                        current.tanggal_kembali = (tgl_lama + timedelta(days=hari)).strftime("%d-%m-%Y")
                        print("Masa sewa berhasil diperpanjang.")
                        return True

                if current.status.lower() == "ready":

                    try:
                        lama_sewa = int(input("Berapa hari ingin menyewa?: "))
                    except ValueError:
                        print("Input harus angka!")
                        return False

                    current.status = "Dipakai"
                    current.penyewa_aktif = nama_penyewa

                    tanggal_sewa = datetime.now()
                    tanggal_kembali = tanggal_sewa + timedelta(days=lama_sewa)

                    current.tanggal_kembali = tanggal_kembali.strftime("%d-%m-%Y")

                    total_biaya = current.harga * lama_sewa

                    data_history = [
                        tanggal_sewa.strftime("%d-%m-%Y %H:%M:%S"),
                        nama_penyewa,
                        current.nama,
                        total_biaya
                    ]

                    history.push(data_history)
                    history.simpan_history(data_history)

                    print("\n===== DETAIL SEWA =====")
                    print(f"Penyewa          : {nama_penyewa}")
                    print(f"Kendaraan        : {current.nama}")
                    print(f"Tanggal Sewa     : {tanggal_sewa.strftime('%d-%m-%Y')}")
                    print(f"Tanggal Kembali  : {current.tanggal_kembali}")
                    print(f"Durasi           : {lama_sewa} hari")
                    print(f"Total Biaya      : Rp{total_biaya}")

                    return True

                else:
                    print(f"\nKendaraan {current.nama} sedang dipakai sampai {current.tanggal_kembali}")

                    pilih_antrean = input("Ingin masuk antrean? (y/n): ")

                    if pilih_antrean.lower() == "y":
                        antrean.enqueue(nama_penyewa, current.id)
                        antrean.simpan_antrean()
                        print("Berhasil masuk antrean.")

                    return False

            current = current.next

        print("ID tidak ditemukan!")
        return False
    

    def update_status_otomatis(self):

        current = self.head

        while current:

            if current.status == "Dipakai" and current.tanggal_kembali != "-":

                tanggal_kembali = datetime.strptime(current.tanggal_kembali, "%d-%m-%Y")

                if datetime.now() >= tanggal_kembali:
                    current.status = "Telat"
                    print(f"\n[NOTIF] {current.nama} TELAT mengembalikan! Unit: {current.nama}")

            current = current.next


    def kembalikan_kendaraan(self, id_kendaraan, antrean, history):

        current = self.head

        while current:

            if current.id.upper() == id_kendaraan.upper():
                
                if current.status == "Dipakai" or current.status == "Telat":
                    denda = 0

                    if current.status == "Telat":
                        tanggal_kembali = datetime.strptime(current.tanggal_kembali, "%d-%m-%Y")

                        selisih_hari = (datetime.now() - tanggal_kembali).days

                        #kurang dari 1 hari dihitung 1 hari
                        if selisih_hari < 1:
                            selisih_hari = 1

                        denda = selisih_hari * 100000


                    print("\n===== DETAIL PENGEMBALIAN =====")
                    print(f"Kendaraan : {current.nama}")
                    print(f"Status    : {current.status}")
                    print(f"Denda     : Rp{denda}")

                    current.status = "Ready"
                    current.tanggal_kembali = "-"
                    current.penyewa_aktif = "-"

                    # Cek Antrean Otomatis
                    node_Antrean = antrean.front

                    if node_Antrean and node_Antrean.id_kendaraan.upper() == current.id.upper():

                        print(f"\n[INFO ANTREAN]:")
                        print(f"{node_Antrean.nama_user} otomatis menyewa {current.nama}")

                        # otomatis sewakan ke user antrean pertama
                        lama_sewa = 1  # default 1 hari

                        current.status = "Dipakai"
                        current.penyewa_aktif = node_Antrean.nama_user

                        tanggal_sewa = datetime.now()
                        tanggal_kembali = tanggal_sewa + timedelta(days=lama_sewa)

                        current.tanggal_kembali = tanggal_kembali.strftime("%d-%m-%Y")

                        # hapus dari antrean
                        antrean.dequeue()
                        antrean.simpan_antrean()
                        
                        total_biaya = current.harga * lama_sewa

                        data_history = [
                            tanggal_sewa.strftime("%d-%m-%Y %H:%M:%S"),
                            node_Antrean.nama_user,
                            current.nama,
                            total_biaya
                        ]

                        history.push(data_history)
                        history.simpan_history(data_history)


                    print("Kendaraan berhasil dikembalikan.")
                    return

                else:
                    print("Kendaraan sedang tidak dipakai.")
                    return

            current = current.next

        print("ID kendaraan tidak ditemukan.")


#======================== Fitur Login & Auth ===================

#cegah username yang duplikat
def username_duplikat(username):

    try:
        with open("dataAkun.txt", "r") as file:
            #cek satu persatu line
            for line in file:
                #jadikan data per line data individual masing masing, dan jadi list
                data = line.strip().split("|")
                #cek apakah username sudah ada di file
                if username == data[0]:
                    return True
                
    except:
        pass

    return False


def register():

    print("\n" + "="*20 + " Register Akun " + "="*20)
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

    print("\n" + "="*20 + " Login Sistem " + "="*20)
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
                    print("Login Berhasil!")
                    return data[0], data[2] # Mengembalikan username dan role
    
    #cegah error file tidak ada
    except FileNotFoundError:
        print("File akun belum ada!")

    print("Username atau password salah.")
    return None, None


# ========================== MAIN PROGRAM ======================================

def main():

    ll = LinkedList()
    ll.load_file()

    history = Stack()
    history.load_history()

    antrean = QueueAntrean() 
    antrean.load_antrean()


    while True:

        role = None
        user_aktif = None

        # Loop Login/Register
        while role is None:

            print("\n" + "="*20 + " Rental Mobil dan Motor Babeh Ipul " + "="*20)
            print("1. Login")
            print("2. Register")
            print("0. Keluar")

            pilih = input("Pilih menu (1-2): ")

            if pilih == "1":
                user_aktif, role = login()
            elif pilih == "2":
                register()
            elif pilih == "0":
                print("Terima kasih telah berkunjung!")
                return
            else:
                print("Pilihan tidak valid.")
        

        # ================= MENU ADMIN BARU =================

        if role == "admin":

            while True:

                ll.update_status_otomatis()

                print("\n" + "="*20 + " DASHBOARD ADMIN " + "="*20)
                print(f"Petugas: {user_aktif}")
                print("-" * 40)
                print("1. Kelola Kendaraan")
                print("2. Transaksi Rental")
                print("3. Data & Riwayat")
                print("4. Logout")
                print("0. Tutup Aplikasi")

                pilih = input("Pilih Menu: ")

                # ================= KELOLA KENDARAAN =================

                if pilih == "1":

                    while True:

                        print("\n" + "="*15 + " KELOLA KENDARAAN " + "="*15)
                        print("1. Tambah Kendaraan")
                        print("2. Tampilkan Kendaraan")
                        print("3. Ubah Kendaraan")
                        print("4. Hapus Kendaraan")
                        print("5. Searching & Sorting")
                        print("0. Kembali")

                        sub = input("Pilih Menu: ")

                        if sub == "1":

                            print("\n======== Tambah Kendaraan ========")
                            id = input("Masukkan ID: ")
                            nama = input("Masukkan Nama Kendaraan: ")
                            jenis = input("Masukkan Jenis (Mobil/Motor): ")

                            try:
                                harga = int(input("Masukkan Harga Sewa: "))
                            except ValueError:
                                print("Harga harus angka!")
                                continue

                            if ll.tambah_kendaraan(id, nama, jenis, harga):
                                ll.simpan_file()
                                print("Kendaraan berhasil ditambahkan!")

                        elif sub == "2":

                            print("\n======== Daftar Kendaraan ========")
                            ll.tampilkan()

                        elif sub == "3":

                            id = input("Masukkan ID kendaraan yang ingin diubah: ")
                            ll.ubah_kendaraan(id)
                            ll.simpan_file()

                        elif sub == "4":

                            id = input("Masukkan ID kendaraan yang ingin dihapus: ")
                            ll.hapus_kendaraan(id)
                            ll.simpan_file()

                        elif sub == "5":

                            while True:

                                ll.tampilkan()

                                print("\n1. Cari berdasarkan Nama")
                                print("2. Cari berdasarkan Status")
                                print("3. Cari berdasarkan Jenis")
                                print("4. Urutkan Nama A-Z")
                                print("5. Urutkan Nama Z-A")
                                print("6. Urutkan Harga Termurah")
                                print("7. Urutkan Harga Termahal")
                                print("8. Urutkan Status")
                                print("0. Kembali")

                                pilih_sort = input("Pilih menu: ")

                                if pilih_sort == "1":
                                    keyword = input("Masukkan nama kendaraan: ")
                                    ll.cari_kendaraan_nama(keyword)

                                elif pilih_sort == "2":
                                    keyword = input("Masukkan status kendaraan: ")
                                    ll.cari_kendaraan_status(keyword)

                                elif pilih_sort == "3":
                                    keyword = input("Masukkan jenis kendaraan: ")
                                    ll.cari_kendaraan_jenis(keyword)

                                elif pilih_sort == "4":
                                    ll.sort_by_name_asc()
                                    ll.tampilkan()

                                elif pilih_sort == "5":
                                    ll.sort_by_name_dsc()
                                    ll.tampilkan()

                                elif pilih_sort == "6":
                                    ll.sort_by_price_asc()
                                    ll.tampilkan()

                                elif pilih_sort == "7":
                                    ll.sort_by_price_dsc()
                                    ll.tampilkan()

                                elif pilih_sort == "8":
                                    ll.sort_by_status()
                                    ll.tampilkan()

                                elif pilih_sort == "0":
                                    break

                                else:
                                    print("Pilihan tidak valid.")

                        elif sub == "0":
                            break

                        else:
                            print("Pilihan tidak valid.")


                # ================= TRANSAKSI RENTAL =================

                elif pilih == "2":

                    while True:

                        print("\n" + "="*15 + " TRANSAKSI RENTAL " + "="*15)
                        print("1. Sewa Kendaraan")
                        print("2. Pengembalian Kendaraan")
                        print("3. Lihat Kendaraan Disewa")
                        print("0. Kembali")

                        sub = input("Pilih Menu: ")

                        if sub == "1":

                            ll.tampilkan()
                            id_sewa = input("Masukkan ID kendaraan yang ingin disewa: ")

                            if ll.sewa_kendaraan(id_sewa, user_aktif, history, antrean):
                                ll.simpan_file()

                        elif sub == "2":

                            ll.tampilkan_khusus_sewa()

                            id_kembali = input("\nMasukkan ID kendaraan yang dikembalikan: ")

                            ll.kembalikan_kendaraan(id_kembali, antrean, history)
                            ll.simpan_file()

                        elif sub == "3":

                            ll.tampilkan_khusus_sewa()

                        elif sub == "0":
                            break

                        else:
                            print("Pilihan tidak valid.")


                # ================= DATA & RIWAYAT =================

                elif pilih == "3":

                    while True:

                        print("\n" + "="*15 + " DATA & RIWAYAT " + "="*15)
                        print("1. Riwayat Sewa")
                        print("2. Lihat Antrean")
                        print("3. Cek Tanggal Hari Ini")
                        print("0. Kembali")

                        sub = input("Pilih Menu: ")

                        if sub == "1":

                            history.tampilkan()

                        elif sub == "2":

                            antrean.tampilkan_antrean()

                        elif sub == "3":

                            print(f"\nTanggal Hari Ini: {datetime.now().strftime('%d %B %Y')}")

                        elif sub == "0":
                            break

                        else:
                            print("Pilihan tidak valid.")

                elif pilih == "4":

                    print("Logout berhasil...")
                    break

                elif pilih == "0":

                    return

                else:

                    print("Pilihan tidak valid.")



       # ================= MENU USER BARU =================

        elif role == "user":

            while True:

                ll.update_status_otomatis()

                print("\n" + "="*20 + " MENU PELANGGAN " + "="*20)
                print(f"Penyewa: {user_aktif}")
                print("-" * 40)
                print("1. Daftar Kendaraan")
                print("2. Searching & Sorting")
                print("3. Rental Saya")
                print("4. Logout")
                print("0. Tutup Aplikasi")

                pilih = input("Pilih Menu: ")

                # ================= DAFTAR KENDARAAN =================

                if pilih == "1":

                    while True:

                        print("\n" + "="*15 + " DAFTAR KENDARAAN " + "="*15)
                        print("1. Tampilkan Semua Kendaraan")
                        print("2. Tampilkan Kendaraan Disewa")
                        print("0. Kembali")

                        sub = input("Pilih Menu: ")

                        if sub == "1":

                            ll.tampilkan()

                        elif sub == "2":

                            ll.tampilkan_khusus_sewa()

                        elif sub == "0":

                            break

                        else:

                            print("Pilihan tidak valid.")


                # ================= SEARCHING & SORTING =================

                elif pilih == "2":

                    while True:

                        ll.tampilkan()

                        print("\n1. Cari berdasarkan Nama")
                        print("2. Cari berdasarkan Status")
                        print("3. Cari berdasarkan Jenis")
                        print("4. Urutkan Nama A-Z")
                        print("5. Urutkan Nama Z-A")
                        print("6. Urutkan Harga Termurah")
                        print("7. Urutkan Harga Termahal")
                        print("8. Urutkan Status")
                        print("0. Kembali")

                        sub = input("Pilih menu: ")

                        if sub == "1":

                            keyword = input("Masukkan nama kendaraan: ")
                            ll.cari_kendaraan_nama(keyword)

                        elif sub == "2":

                            keyword = input("Masukkan status kendaraan: ")
                            ll.cari_kendaraan_status(keyword)

                        elif sub == "3":

                            keyword = input("Masukkan jenis kendaraan: ")
                            ll.cari_kendaraan_jenis(keyword)

                        elif sub == "4":

                            ll.sort_by_name_asc()
                            ll.tampilkan()

                        elif sub == "5":

                            ll.sort_by_name_dsc()
                            ll.tampilkan()

                        elif sub == "6":

                            ll.sort_by_price_asc()
                            ll.tampilkan()

                        elif sub == "7":

                            ll.sort_by_price_dsc()
                            ll.tampilkan()

                        elif sub == "8":

                            ll.sort_by_status()
                            ll.tampilkan()

                        elif sub == "0":

                            break

                        else:

                            print("Pilihan tidak valid.")


                # ================= RENTAL SAYA =================

                elif pilih == "3":

                    while True:

                        print("\n" + "="*15 + " RENTAL SAYA " + "="*15)
                        print("1. Sewa Kendaraan")
                        print("2. Riwayat Sewa Saya")
                        print("3. Lihat Antrean")
                        print("0. Kembali")

                        sub = input("Pilih Menu: ")

                        if sub == "1":

                            ll.tampilkan()

                            id_sewa = input("Masukkan ID kendaraan yang ingin disewa: ")

                            if ll.sewa_kendaraan(id_sewa, user_aktif, history, antrean):
                                ll.simpan_file()

                        elif sub == "2":

                            print(f"\nTanggal Hari Ini: {datetime.now().strftime('%d %B %Y')}")
                            history.tampilkan_history_user(user_aktif)

                        elif sub == "3":

                            antrean.tampilkan_antrean()

                        elif sub == "0":

                            break

                        else:

                            print("Pilihan tidak valid.")


                # ================= LOGOUT =================

                elif pilih == "4":

                    print("Logout berhasil...")
                    break


                # ================= TUTUP APLIKASI =================

                elif pilih == "0":

                    return


                else:

                    print("Pilihan tidak valid.")



if __name__ == "__main__":
    main()
