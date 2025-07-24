import main
from services.db import insert_item, fetch_item, delete_item, update_item, get_item_by_code


def add():
    try:
        kode_barang = input("kode_barang: ")
        nama_barang = input("nama_barang: ")
        
        while True:
            try:
                harga_barang = int(input("harga_barang: "))
                break  # Keluar dari loop jika berhasil convert ke int
            except ValueError:
                print("Error: Stok barang harus berupa angka! Silahkan coba lagi.")
        
        # Loop sampai user memasukkan angka yang valid
        while True:
            try:
                stok_barang = int(input("stok_barang: "))
                break  # Keluar dari loop jika berhasil convert ke int
            except ValueError:
                print("Error: Stok barang harus berupa angka! Silahkan coba lagi.")
        
        insert_item(kode_barang, nama_barang, harga_barang, stok_barang)
        
    except KeyboardInterrupt:
        print("\nOperasi dibatalkan.")
    except Exception as e:
        print(f"Error: {e}")

def check():
    try:
        items = fetch_item()  
        if items:  # Cek apakah ada data
            print("\t\t=== DAFTAR BARANG ===") 
            print("Kode\t| Nama Barang\t| Harga Barang\t| Stok\t")
            print("-" * 55)
            for item in items:
                print(f"{item[1]}\t| {item[2]}\t\t| {item[3]}\t\t| {item[4]}")
        else:
            print("Tidak ada data barang dalam database.")
    except Exception as e:
        print(f"Error saat mengambil data: {e}")

def update():
    try:
        check()
        kode_barang = input("\nMasukkan kode barang yang akan diupdate: ")
        item = get_item_by_code(kode_barang)
        if item:
            print(f"\nData saat ini:")
            print(f"Kode Barang: {item[1]}")
            print(f"Nama Barang: {item[2]}")
            print(f"Harga Barang: {item[3]}")
            print(f"Stok Barang: {item[4]}")
            
            # Input nama barang baru
            nama_barang_baru = input(f"\nNama barang baru dengan kode ({item[2]}): ")
            if not nama_barang_baru:
                nama_barang_baru = item[2]
            
            # Input harga barang baru
            while True:
                try:
                    harga_input = input(f"Harga barang baru ({item[3]}): ")
                    if not harga_input:
                        harga_barang_baru = item[3]
                        break
                    else:
                        harga_barang_baru = int(harga_input)
                        break
                except ValueError:
                    print("Error: Harga barang harus berupa angka! Silahkan coba lagi.")
            
            # Input stok barang baru
            while True:
                try:
                    stok_input = input(f"Stok barang baru ({item[4]}): ")
                    if not stok_input:
                        stok_barang_baru = item[4]
                        break
                    else:
                        stok_barang_baru = int(stok_input)
                        break
                except ValueError:
                    print("Error: Stok barang harus berupa angka! Silahkan coba lagi.")
            
            # Konfirmasi update
            konfirmasi = input(f"\nApakah Anda yakin ingin mengupdate barang dengan kode '{kode_barang}'? (ya/tidak): ")
            
            if konfirmasi.lower() == "ya": 
                if update_item(kode_barang, nama_barang_baru, harga_barang_baru, stok_barang_baru):
                    print("Update berhasil!")
                else:
                    print("Update gagal!")
            else:
                print("Update dibatalkan.")
        else:
            print(f"Barang dengan kode '{kode_barang}' tidak ditemukan!")
    except KeyboardInterrupt:
        print("\nOperasi dibatalkan.")

def delete():
    try:
        check()
        kode_barang = input("\nmasukan kode barang yang akan di hapus : ")
        konfirmasi = input(f"apakah kamu yakin menghapus barang dengan kode {kode_barang} ? (ya/tidak): ")
        if konfirmasi.lower() == "ya": #lower untuk mentolerir semua kata kecuali kata acak selain kata yang sudah di tentukan
            if delete_item(kode_barang):
                print(f"barang dengan kode '{kode_barang}' telah di hapus")
            else:
                print("penghapusan gagal!")
        else:
            print("penghapusan dibatalkan")
            
    except  KeyboardInterrupt:
        print("operasi dibatalkan")

def start():
    while True:
        try:
            menu = int(input(f'''
menu program :
1. Tambah Barang
2. Check Barang
3. Update Barang
4. Hapus Barang
5. Kembali
Silahkan pilih: '''))
            
            if menu == 1:
                add()
            elif menu == 2:
                check()
            elif menu == 3:
                update()
            elif menu == 4:
                delete()
            elif menu == 5:
                print("kembali ke menu utama")
                main.options()
                break
            else:
                print("Pilihan tidak valid! Silahkan pilih nomor 1-5")
                
        except ValueError:
            print("Error: Pilihan harus berupa angka!")
        except KeyboardInterrupt:
            print("\nProgram dihentikan.")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    start()

