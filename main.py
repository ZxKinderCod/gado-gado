from libswel import screen_welcome, screen_exit
def options():
    user_option = int(input(f'''menu program yang tersedia:
1. Games Bitcoin 
2. Kios Sederhana
3. Keluar program
silahkan pilih: '''))
    
    # user_option=options()
    if user_option == 1:
        screen_welcome("Selamat datang di ₿itcoin Game")
        from games import bitcoin
        bitcoin.start()
    elif user_option == 2:
        import kios
        kios.start()
    elif user_option == 3:
        screen_exit()
        exit()
        
    else:
        print("hanya boleh pilih menu yang tersedia")


def main():
    # user_option=options()
    # if user_option == 1:
    #     screen_welcome("Selamat datang di ₿itcoin Game")
    #     from games import bitcoin
    #     bitcoin.start()
    # elif user_option == 2:
    #     import kios
    #     kios.start()
    # else:
    #     print("hanya boleh pilih menu yang tersedia")
    options()  #jgn di hapus
    # screen_exit()




if __name__ == "__main__":
    main()

