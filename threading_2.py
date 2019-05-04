import threading
from queue import Queue
import time

print_lock = threading.Lock()

def exapleJob(worker):
	time.sleep(0.5)
	with print_lock:
		print(threading.current_thread().name, worker)



q = Queue()


#Setting up 10 Threads , threding function is threader   
def threader():
	while True:
		worker =q.get()
		exapleJob(worker)
		q.task_done()

for x in range(10): # we are stating 10 Threads 
	t = threading.Thread(target = threader)
	t.deamon = True
	t.start()




start = time.time()

for worker in range (20):
	q.put(worker)


q.join()

print ("Entire job took: ",time.time() - start)