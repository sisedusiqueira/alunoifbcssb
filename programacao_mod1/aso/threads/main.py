import threading
import time

def thread(nome):
    for index in range(10):
        time.sleep(0.1)
    print(nome,end="")

print("inicio da thread main")
t1 = threading.Thread(target=thread,args=("T1",))
t2 = threading.Thread(target=thread,args=("T2",))
t3 = threading.Thread(target=thread,args=("T3",))


t1.start()
t2.start()
t1.join()
t2.start()

#t1.join()
print("Fim da main")

