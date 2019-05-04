import time
import threading

def print_time(ThreadName, delay):
	count = 0;
	while count<5:
		time.sleep(delay)
		count +=1
		print (ThreadName, time.ctime(time.time()))

def print_time2(ThreadName, delay):
	count = 0;
	while 1:
		time.sleep(delay)
		count +=1
		print (ThreadName, time.ctime(time.time()))


t1 = threading.Thread(target =print_time , args = ("Thread 1" , 2 ,))
t2 = threading.Thread(target =print_time2 , args = ("Thread 2 Loop" , 4 ,))

t1.start()
t2.start()

t1.join()
t2.join()
while 1:
	print("A")
	time.sleep(1)
