from time import  sleep
from threading import *


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

t1 = Hi()
t2 = Hello()
t1.start()
sleep(.2)
t2.start()

t1.join()
t2.join()

print("Bye")