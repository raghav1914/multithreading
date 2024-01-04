import threading

def a():
    while True:
        print("aaaaa")

def b():
    while True:
        print("bbbbb")

# Create thread objects for each function
thread1 = threading.Thread(target=a)
thread2 = threading.Thread(target=b)

# Start the threads
thread1.start()
thread2.start()

# Keep the main thread running
while True:
    pass
