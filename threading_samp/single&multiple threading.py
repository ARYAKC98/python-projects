"""single threading"""
# from time import sleep
# def task(sleep_time,message):
#     sleep(sleep_time)
#     print(message)
#
# from threading import Thread
# thread=Thread(target=task,args=(1.5,'new message here'))
# thread.start()


"""multiple threading"""

import time   #import time module
import threading

def cal_sqre(num):      #define a cal_sqre function
    print("calculate the sqaure root of the given number")
    for n in num:
        time.sleep(0.3)    #at each iteration it waits for 0.3 sec time
        print("sqauare is:",n*n)

def cal_cube(num):
    print("calculate the cube of given number")
    for n in num:
        time.sleep(0.3)
        print("cube is:",n*n*n)
arr = [4,5,6,7,2]    #given array or list

t1 = time.time()    #get total time to execute the function
th1 = threading.Thread(target=cal_sqre,args=(arr,))
th2 = threading.Thread(target=cal_cube,args=(arr,))
th1.start()
th2.start()
th1.join()
th2.join()
print("total time taken by threads is:",time.time()-t1)     #print the total time