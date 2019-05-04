

import threading 

def do_this():
	global x
	print ("This is our Thread")
	while x<300:
		x +=1
	print(x)

def do_after():
	global x
	while x<600:
		x +=1
	print(x)

def main():
	global x
	x  = 0 

	our_thread = threading.Thread( target = do_this,name = 'Our Thread')
	our_thread.start()
	our_thread.join() #this join the thread with the below thread , So only once this complete execution,below will start execute


	our_next_thread = threading.Thread (target = do_after)
	our_next_thread.start()
	
	print(threading.active_count())
	print(threading.enumerate())




if ( __name__ == "__main__"):
	main()
