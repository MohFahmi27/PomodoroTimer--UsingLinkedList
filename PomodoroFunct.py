import time
from playsound import playsound
from QueueLinkedlist import Queue

duration = 25 # durasi 1 task pomodoro
short_brk = 5  # short break duration
long_brk = 15  # task > 4:long break duration
duration_count = duration
Q = Queue()

def pomodoro(banyak_tugas, short_brk, long_brk, duration, duration_count):
    task_count = 0
    for i in range(1, banyak_tugas+1):
        duration = duration_count
        while duration > 0:
            print ("%d MIN WORKING" % int(duration_count - duration))
            time.sleep(60)
            duration -= 1
            task_count += 1
        playsound('sound/finishtask.mp3')
        task_count = task_count
        Q.de__queue()

        if task_count == banyak_tugas:
            print("Last Task")
            time.sleep(25*60)
            playsound('sound/finishsession.mp3')
            print("=============POMODORO FINISHED============")
        elif task_count % 4 == 0:
            # long break
            playsound('sound/breakfifteenmin.mp3')
            print("Take long %d min break" % long_brk)
            time.sleep(60*int(long_brk))
        else:
            # short break
            playsound('sound/breakfivemin.mp3')
            print ("%d MIN BREAK" % short_brk)
            time.sleep(60*int(short_brk))
            print("BACK TO WORK")
            playsound('sound/breakover.mp3')