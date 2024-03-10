class Node:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
        self.next = None

class Keranjang:
    def __init__(self):
        self.head = None

    def tambah_pesanan(self, nama, harga):
        new_node = Node(nama, harga)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    print(" SELAMAT DATANG DI E-ORDER WARUNG D4 MI")
    print("MINUMAN DAN MIE PEDAS TERSEDIA DI SINI!!  ")

    def tampilkan_pesanan(self):
        if not self.head:
            print("Keranjang masih kosong.")
            return

        print("\nPesanan yang sudah ditambahkan:")
        print("+----+------------------------+--------+")
        print("| No |       Nama Menu        | Harga  |")
        print("+----+------------------------+--------+")

        current = self.head
        index = 1
        while current:
            print(f"| {index:2} | {current.nama.capitalize():24} | {current.harga:6} |")
            current = current.next
            index += 1

        print("+----+------------------------+--------+")

    def total_harga(self):
        total = 0
        current = self.head
        while current:
            total += current.harga
            current = current.next
        return total

# Menu Miexue
menu = {
    'miexue ice cream': 5000,
    'boba shake': 16000,
    'mi sundae': 14000,
    'mi ganas': 11000,
    'creamy mango boba': 22000
}

keranjang = Keranjang()

print("\nMenu Miexue:")
print("+----+------------------------+--------+")
print("| No |       Nama Menu        | Harga  |")
print("+----+------------------------+--------+")

for index, (item, harga) in enumerate(menu.items(), start=1):
    print(f"| {index:2} | {item.capitalize():24} | {harga:6} |")

print("+----+------------------------+--------+")

print("Silakan pilih menu yang ingin dipesan atau ketik 'done' untuk selesai.")

while True:
    pilihan = input("Masukkan menu yang ingin dipesan: ").strip().lower()

    if pilihan == 'done':
        break

    if pilihan not in menu:
        print("Menu tidak valid, silakan pilih lagi.")
        continue

    keranjang.tambah_pesanan(pilihan, menu[pilihan])
    print(f"{pilihan.capitalize()} sudah ditambahkan ke keranjang.")

keranjang.tampilkan_pesanan()

if keranjang.head:
    total_biaya = keranjang.total_harga()
    print(f"\nTotal biaya yang harus dibayarkan adalah {total_biaya} rupiah")
    print (" Terimakasih sudah memesan :)")
else:
    print("\nAnda belum memesan apapun. Terima kasih!") 
