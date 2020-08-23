# time.time() returns ticks (current time in seconds) . It tells the current seconds.

import time

initial = time.time()
k = 0
while k < 45:
    print("Hello This is Aditya Mukherjee")
    time.sleep(2)  # sleeps for 2 seconds
    k += 1
print(f"Time Taken by while loop {time.time() - initial} seconds")

initial2 = time.time()
for i in range(45):
    print("Hello This is Aditya Mukherjee")
print(f"Time Taken by for loop {time.time()- initial2} seconds")


localtime = time.asctime(time.localtime(time.time()))
print(localtime)
