import random

import main


print('''Selamat datang di mini-game sederhana: Cari ₿itcoin Tersembunyi!
Kamu akan melihat 5 cold wallet yang tampak sama (💳).
Tapi... hanya satu di antaranya yang menyimpan ₿itcoin!
Setiap kali kamu bermain, isi dan posisi ₿itcoin akan dipilih secara acak.
Siap menebak di mana letaknya?
    ''')
print("Apakah kamu mau bermain? (yes / no)")
input_user = input("Jawabanya: ")
if input_user=="no":
    print("Yahhh... padahal seru loh")
    exit()
elif input_user=="yes":
    print(f'''Terima kasih sudah memilih dan selamat bermain 
          ''')
else:
    print("program ini berhenti karena jawaban mu gajelas pea")
    exit()
nama_user = input("Masukkan nama kamu: ")
while nama_user == "":
    print("Nama tidak boleh kosong, silahkan masukan nama kamu")
    nama_user = input("Masukan nama kamu: ")

print("Selamat datang di zona rahasia, tebak dengan tepat dan raih ₿itcoin yang tersembunyi di dalamnya! ")
def start():
    while True:

        print('''Selamat datang di mini-game sederhana: Cari ₿itcoin Tersembunyi!
Kamu akan melihat 5 cold wallet yang tampak sama (💳).
Tapi... hanya satu di antaranya yang menyimpan ₿itcoin!
Setiap kali kamu bermain, isi dan posisi ₿itcoin akan dipilih secara acak.
Siap menebak di mana letaknya?
    ''')
        
        bentuk_wallet = "💳"
        wallet_kosong = [bentuk_wallet] * 5
        cold_wallet = wallet_kosong.copy()
        btc_position = random.randint(1, 5)
        hasil_tampil = " ".join(wallet_kosong)
        cold_wallet[btc_position - 1] = "₿"
        hasil_akhir_jawaban = " ".join(cold_wallet)

        print(f'''Hai {nama_user} coba perhatikan cold wallet di bawah ini
    {hasil_tampil}''')

        pilihan_kamu = int( input(f"Menurut {nama_user} cold wallet manakah yang menyimpan ₿itcoin? [1 / 2 / 3 / 4 / 5 ] "))
        print(f"pilihan kamu adalah nomor {pilihan_kamu}")

        while pilihan_kamu < 1 or pilihan_kamu > 5:
            print("Pilihan kamu tidak valid, silahkan pilih nomor antara 1 sampai 5")
            pilihan_kamu = int(input("Masukan pilihan kamu: "))

        print(F'''Apakah {nama_user} yakin dengan pilihan nomor {pilihan_kamu} ? (yakin / masih ragu)''') 
        input_konfirmasi = input("Jawabanya: ")
        if input_konfirmasi == "masih ragu":
            print("program akan berhenti")
            # break
            exit()
        elif input_konfirmasi == "yakin":
            if pilihan_kamu == btc_position:
                print(f'''Kamu benar🏆🔥! ₿itcoin berada di {hasil_akhir_jawaban} nomor {btc_position} 
    dan jawabanmu adalah {pilihan_kamu}
        ''')
            else:
                print(f'''Uncccchh kamu salah 😜 wleeeee! ₿itcoin berada di {hasil_akhir_jawaban} nomor {btc_position} 
    tetapi jawabanmu adalah nomor {pilihan_kamu}, silahkan coba lagi
        ''')
        else:
            print("Jawaban tidak valid, silahkan coba lagi dan program ini berhenti")
            # break
            exit()
        bermain_lagi = input("Apakah kamu mau bermain lagi? (ya / tidak) ")
        if bermain_lagi.lower() == "tidak":
            main.options()
            break

if __name__ == "__main__":
    start()