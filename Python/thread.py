import threading
import time
import concurrent.futures

##############################################
"""def func():
    print("ran")
    time.sleep(1)
    print("done")
    time.sleep(0.85)
    print("now done")

x = threading.Thread(target = func)
x.start()
print(threading.activeCount())
time.sleep(1.2)
print("finally")"""

############################################

"""def count(n):
    for i in range(1, n + 1):
        print(i)
        time.sleep(0.01)

def count2(n):
    for i in range(1, n + 1):
        print(i)
        time.sleep(0.02)

x = threading.Thread(target=count, args=(10,))
x.start()

y = threading.Thread(target=count2, args=(10,))
y.start()

print("Done")"""

##########################################

"""ls = []

def count(n):
    for i in range(1, n + 1):
        ls.append(i)
        time.sleep(0.5)

def count2(n):
    for i in range(1, n + 1):
        ls.append(i)
        time.sleep(0.5)

x = threading.Thread(target=count, args=(5,))
x.start()
x.join()

y = threading.Thread(target=count, args=(5,))
y.start()

y.join()

print(ls)"""

###############################################

'''class My_Thread(threading.Thread):

    def __init__(self, threadID, name, counter):

        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):

        print("Starting " + self.name + "\n")
        print_time(self.name, self.counter, 5)
        print("Exiting " + self.name + "\n")

def print_time(threadName, delay, counter):

    while counter:

        time.sleep(delay)
        print("%s : %s %s" % (threadName, time.ctime(time.time()), counter), "\n")
        counter -= 1

# Create new threads
thread1 = My_Thread(1, "Payment", 3)
thread2 = My_Thread(2, "Sending Email", 5)
thread3 = My_Thread(3, "Loading page", 1.5)


# Start new threads
thread1.start()
thread1.join()
thread2.start()
thread3.start()
thread2.join()
thread3.join()


print("Exiting main thread")'''

####################################################################

class My_Thread(threading.Thread):

    def __init__(self, threadID, name, counter):

        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):

        print("Starting " + self.name + "\n")
        ThreadLock.acquire()                         # Locks the thread and do not allow any other thread to run
        print_time(self.name, self.counter, 3)
        ThreadLock.release()                         # After the fuction, it releases it and then any other thread can run
        print("Exiting " + self.name + "\n")


class My_Thread2(threading.Thread):

    def __init__(self, threadID, name, counter):

        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):

        print("Starting " + self.name + "\n")
        ThreadLock.acquire()                        
        print_time(self.name, self.counter, 3)
        print("Exiting " + self.name + "\n")

def print_time(threadName, delay, counter):

    while counter:

        time.sleep(delay)
        print("%s : %s %s" % (threadName, time.ctime(time.time()), counter), "\n")
        counter -= 1

ThreadLock = threading.Lock()

# Create new threads
thread1 = My_Thread(1, "Payment", 4)
thread2 = My_Thread2(2, "Sending Email", 5)
thread3 = My_Thread2(3, "Loading page", 2)

# thread1.start()
# thread2.start()
# thread3.start()
# thread1.join()
# thread2.join()
# thread3.join()
# print("Done main thread")

##########################################################################################################################

def do_something(seconds):
    print(f"sleeping {seconds} second(s)...")
    time.sleep(seconds)
    return "Done sleeping..."

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_something, 2)     # Creates a future object; 2 is the argument for the function
    print(f1.result())                        # Prints the return of function

    secs = list(range(1, 6))
    output = executor.map(do_something, secs) #  

threads = []

# Creates 10 threads of do_something function

for _ in range(5):
    t = threading.Thread(target=do_something, args=(1.2,))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
