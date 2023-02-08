#python threads
#normal
from time import sleep
def task():
    #block for a moment(here 2 sec)
    sleep(2)
    #display a message
    print("this is from another thread")
# task()


#using threading
from threading import Thread
#create thread
thread = Thread(target=task)
#next ,we can create an instance of the threading.thread class and specify
#our function name as the "target" argument in the constructor
#run the thread
thread.start()


