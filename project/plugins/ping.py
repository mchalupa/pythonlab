#!/usr/bin/python

import threading
import Queue
import time

queue = Queue.Queue()

class PingThread(threading.Thread):
	def __init__(self, intf):
		self._inf = intf
		threading.Thread.__init__(self)
		
	def run(self):
		global queue
		
		while True:
			msg = queue.get()
			if msg == "ping=off":
				break
				
			time.sleep(3)
			self._inf.write("pong " + msg)
		
		

def cmd_ping(msg):
	global queue
	
	queue.put(msg)
