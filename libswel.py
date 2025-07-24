from time import sleep

def screen_welcome(judul):
    style = "*" * (len(judul) + 6)

    print(style)
    print(f"** {judul} **")
    print(style)

def screen_exit():
    print('Program ini berhenti')
    sleep(1)
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    sleep(1)
    print("Sampai jumpa lagi!")


if __name__ == "__main__":
    screen_welcome("Selamat datang di ₿itcoin game")
    screen_exit()
