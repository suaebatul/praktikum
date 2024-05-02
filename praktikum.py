#daftar barang beserta harganya
daftar_barang ={
    "Beras": 10000,
    "Gula":8000,
    "Telur":2000,
    "minyak goreng":15000,
    "garam":5000,
    }
#menampilkan daftar barang
print ("daftar barng:")
for barang, harga in dftar_baraang.items():
    print(f"{barang}: Rp {harga}")

#input jumlah barang yang di beli
    total_belanja = 0
    jumlah_barang = int(input("\nmasukan jumlah barang yang dibeli:"))

#menghitung total belanjaan
    for i in range(jumlah_barang):
        barang = input(f"masukan nama barang ke-{i+1}:")
        if barang in daftar_barang:
            total_belanja += dafta_barang[barang]
        else:
                print(f"{barang} tidak ada dalam daftar barang.")

 #menampilkan total belanjaan
                print(f"\ntotal belanjaan anda: Rp {total_belanja}")
