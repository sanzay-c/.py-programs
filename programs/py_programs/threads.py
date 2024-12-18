import threading
import time

# start(): Initiates the thread and begins its execution.
# join(): This method is used to wait for a thread to finish its execution. Blocks the calling thread until the thread on which join() was called has finished.

def print_number():
    for i in range(1, 10):
        print(i)

thread =  threading.Thread(target=print_number)
thread.start()
thread.join()

print("Thread has finished execution")

# ------------------------------------------

class NumberPrinter(threading.Thread):
    def run(self):
        for i in range(10):
            print(i)

thread = NumberPrinter()
thread.start()
thread.join()

# ------------------------------------------

lock = threading.Lock()

def thread_function():
    with lock:
        # Critical section of code
        print("Thread-safe operation")

thread1 = threading.Thread(target=thread_function)
thread2 = threading.Thread(target=thread_function)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

# ------------------------------------------

# ---Events in thread
event =  threading.Event()

def wait_for_event():
    print("waiting for event")
    event.wait()
    print("Event received ")


def set_event():
    time.sleep(2)
    event.set()
    print("Event set ")


t1 = threading.Thread(target=wait_for_event)
t2 = threading.Thread(target=set_event)

t1.start()
t2.start()

t1.join()
t2.join()

# ------------------------------------------

#---Threads can be set as daemon threads, meaning they will not prevent the program from exiting if they are still running. 
#   Daemon threads are useful for background tasks:

def background_task():
    while True:
        time.sleep(2)
        print("Running task in the background")

thread = threading.Thread(target=background_task)

# Set the thread as a daemon thread. This means the thread will run in the background and
# will not prevent the program from exiting. Daemon threads are stopped when the main
# program exits.
thread.daemon = True
thread.start()

time.sleep(5)  # Pause the main thread for 5 seconds
print("Main thread ending")