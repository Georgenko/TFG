#encoding:utf-8

import threading



"""def funcion(a):
    print(f"estoy en una hebra aparte: {a}")
x=threading.Thread(target=funcion,args=(1,))
x.start()
print("estoy en la hebra principal")"""



"""class Hebra(threading.Thread):
    def __init__(self,argumento):
        threading.Thread.__init__(self)
        self.argumento=argumento
    def run(self):
        print(self.argumento)
h=Hebra("test")
h.start()"""



"""COUNTER=0
def increment(n):
    global COUNTER
    for _ in range(n):
        COUNTER+=1
threads=[threading.Thread(target=increment,args=(1000000,)) for _ in range(3)]
[t.start() for t in threads];
[t.join() for t in threads];
print(COUNTER)"""



"""lock=threading.Lock()
COUNTER=0
def increment(n,lock):
    global COUNTER
    for _ in range(n):
        lock.acquire()
        COUNTER+=1
        lock.release()
threads=[threading.Thread(target=increment,args=(1000000,lock)) for _ in range(3)]
[t.start() for t in threads];
[t.join() for t in threads];
print(COUNTER)"""



"""lock=threading.Lock()
COUNTER=0
def increment(n,lock):
    global COUNTER
    for _ in range(n):
        lock.acquire()
        print(lock.locked())
        try:
            raise Exception("excepción")
            COUNTER+=1
        finally:
            lock.release()
threads=[threading.Thread(target=increment,args=(1000000,lock)) for _ in range(3)]
[t.start() for t in threads];
[t.join() for t in threads];
print(COUNTER)
print(lock.locked())"""



"""lock=threading.Lock()
COUNTER=0
def increment(n,lock):
    global COUNTER
    for _ in range(n):
        with lock:
            COUNTER+=1
threads=[threading.Thread(target=increment,args=(1000000,lock)) for _ in range(3)]
[t.start() for t in threads];
[t.join() for t in threads];
print(COUNTER)"""



