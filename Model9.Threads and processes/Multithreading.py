import threading

def worker(x):
    print(x * x)

t1 = threading.Thread(target=worker, args=(1,))
t2 = threading.Thread(target=worker, args=(2,))

t1.start()
t2.start()

t1.join()
t2.join()
