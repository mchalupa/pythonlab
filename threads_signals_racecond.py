#!/usr/bin/python
########################################################################
## THREADS
########################################################################

#import thread # = nizkourovnove API z posix C (nepouzivat, pokud neni nutno)
import threading # = modul nad thread, python rozsireni

class MyThread(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)

  def run(self):
    #my code to be ran in thread


  # pouziti
  th = MyThread()
  th.start()
    "starts the thread and executes self.run(*args) in it"

  def join(self):
    "waits for the running thread to finish"
    
 ======================================== 
|   process |							|
|			|							|
|			|							|
|			|							|
|			start ----| run()			|
|			|			|				|
|			|			|				|
|			|			|				|
|			|			|				|
|			join()		|				|
|			<waiting> --|				|
|			|							|
|			|							|
|										|
 ========================================

# locking
	th.aquire() #zamci
	#  ...
	# do sth...
	#  ...
	th.release()

# vic zamku - vsude zamykat ve stejnem poradi (vsude! v projektu, jinak
# muze dojit k deadlocku)

########################################################################
# POSILANI ZPRAV
########################################################################

# pres frontu
import Queue # je thread-safe
q = Queue.Queue()
q.put() # ceka jenom pokud mame omezenou velikost fronty (nast. v konstruktoru) a ta je plna
q.get() # pokud neni prvek, tak ceka, nez se objevi (na urovni OS ceka, neni to busy-waiting)

#popr.
q.put_nowait()
q.get_nowait()
#neceka, vyhodi vyjimky full/empty

#dalsi varianty
LifoQueue
PriorityQueue # pri get vraci prvek s nejnizsi? hodnotou ve fronte
# porovnava lexikograficky, tzn. muzeme vlozit tuple
# (priorita, id, zprava) ==> podle priority, pak podle id vraci
# od pythona 2.6


