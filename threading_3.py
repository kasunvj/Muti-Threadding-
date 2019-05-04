# NOTE: 
#if you are running a infinite while loop inside a thread, process wornt stop. Ctr+C wont work
#use 		$ pkill python 	to stop 


import threading 

def do_this():
	global dead

	print ("This is our Thread")
	while (not dead):
		pass

def main():
	global dead
	dead = False

	our_thread = threading.Thread( target = do_this)
	our_thread.start()

	print(threading.active_count())
	print(threading.enumerate())
	print (threading.current_thread())

	input("Hit enter to die")
	dead = True


if ( __name__ == "__main__"):
	main()
