import multiprocessing

def work(x):
    print(x)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=work, args=(1,))
    p2 = multiprocessing.Process(target=work, args=(2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()