from threading import Thread
from time import sleep


class Hello(Thread):
    def run(self):
        for i in range(3):
            print("Hello ")
            sleep(1)
class Hi(Thread):
    def run(self):
        for i in range(3):
            print("Hi ")
            sleep(1)
C1 = Hello()
C2 = Hi()
C1.start()
sleep(0.2) #It Prevent Collision
C2.start()
C1.join() #It let continue C1 and C2 output and then print Byee in the end as a job of main Thread, As we have three thread here
C2.join()
print("Byee")