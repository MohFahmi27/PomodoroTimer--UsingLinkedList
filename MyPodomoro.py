from QueueLinkedlist import *
import sys

Q = Queue()

while True :
    print("##############################################")
    print("1. Masukkan Kegiatan.")
    print('2. Lihat Kegiatan')
    print("3. Hapus Kegiatan")
    print("4. Start Pomodoro")
    print("5. Exit")
    print("##############################################")
    user_pil = input("Masukkan pilihan anda : ")

    if user_pil.__eq__("1") :
        req = input("Masukkan Kegiatan : ")
        Q.en_queue(req)
        while True:
            pil = input("apakah anda ingin memasukkan lagi Y/N ")
            if pil.__eq__("Y") or pil.__eq__("y"):
                act = input("Masukkan Kegiatan : ")
                Q.en_queue(act)
            elif pil.__eq__("N") or pil.__eq__("n"):
                break
            else :
                print("Sorry We don't get that")
    elif user_pil.__eq__("2"):
        print("=============================================")
        print("================KEGIATAN ANDA================")
        Q.tampil()
        print("=============================================")

    elif user_pil.__eq__("3") :
        print("=============================================")
        print("================KEGIATAN ANDA================")
        Q.tampil()
        print("=============================================")
        del_keg = input("Masukkan nama Kegiatan yang ingin dihapus : ")
        Q.deleteNode(del_keg)

    elif user_pil.__eq__("4") :
        task = Q.length()
        if task <= 1:
            print("Pekerjaan kosong atau harus lebih satu perkerjaan")
        else:
            from PomodoroFunct import *
            pomodoro(task, short_brk, long_brk, duration, duration_count)
    elif user_pil.__eq__("5"):
        sys.exit(0)
    else :
        print("We don't get that Try Again")