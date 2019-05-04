import threading 
import time

def do_this():
	global dead 
	print("Camera online")
	while (not dead):
		time.sleep(1)
		print(threading.current_thread().name,time.ctime(time.time()))

def do_this_as_well():
	global dead,pos
	print("Traget is Online: ",time.time())
	while (not dead):
		time.sleep(2)
		print(threading.current_thread().name,pos,time.ctime(time.time()))

def change_target():
	global pos
	print(threading.current_thread().name,time.ctime(time.time()))
	pos = [1,1,1]
	time.sleep(2)
	pos = [1,2,31]
	time.sleep(4)
	pos  = [2,34,5]



def main():
	global dead,pos,t
	pos = [0,0,0]
	dead =False

	my_thread = threading.Thread(target = do_this, name = "Camera")
	my_thread.start()

	my_next_thread = threading.Thread(target = do_this_as_well, name ="tareget Pos")
	my_next_thread.start()

	t = time.time()
	target_change_thread = threading.Thread(target = change_target, name= "change taregt")
	target_change_thread.start()
	time.sleep(1)


	pos = [100,200,300]
	time.sleep(2)

	pos = [3400,345,134]
	time.sleep(2)

	print(threading.active_count())

	input("Press Enter to die")
	dead = True

	

		


if(__name__ == "__main__"):
	main()
