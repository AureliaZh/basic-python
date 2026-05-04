import threading

def work(x):
    print(x)

t1 = threading.Thread(target=work, args=(1,))
t2 = threading.Thread(target=work, args=(2,))

t1.start()
t2.start()

t1.join()
t2.join()

def work(x):
    print(x * x)

work(1)
work(2)
work(3)
