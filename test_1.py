import COMP_3_3_MODEL
import numpy as np
from timeit import default_timer as timer
from multiprocessing import Process

l = 3
p = 1

#-------------------------------------------------------

start = timer()

def linear():
    for x in range(l):
        COMP_3_3_MODEL.script9_func()
        print('[]')

p1 = Process(target=linear)
p2 = Process(target=linear)
p3 = Process(target=linear)
p4 = Process(target=linear)
p5 = Process(target=linear)
p6 = Process(target=linear)
p7 = Process(target=linear)
p8 = Process(target=linear)
p9 = Process(target=linear)
p10 = Process(target=linear)


if __name__ == '__main__':
    if p ==1:
        p1.start()
        p1.join()
    elif p==2:
        p1.start()
        p2.start()
        p1.join()
        p2.join()
    elif p == 3:
        p1.start()
        p2.start()
        p3.start()
        p1.join()
        p2.join()
        p3.join()
    elif p == 4:
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
    elif p == 5:
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
    elif p == 6:
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        p6.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()
    elif p == 7:
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        p6.start()
        p7.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()
        p7.join()
    elif p == 8:
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        p6.start()
        p7.start()
        p8.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()
        p7.join()
        p8.join()
    elif p == 9:
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        p6.start()
        p7.start()
        p8.start()
        p9.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()
        p7.join()
        p8.join()
        p9.join()
    elif p == 10:
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        p6.start()
        p7.start()
        p8.start()
        p9.start()
        p10.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()
        p7.join()
        p8.join()
        p9.join()
        p10.join()

end = timer()
t = (end - start)
print(t)