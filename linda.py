from threading import Lock
import _thread

Ts = {}
mutex = Lock()
nb_threads = 0

def Out(name, elem):
	global Ts
	nouvElems = {name: elem}
	Ts.update(nouvElems)
	if mutex.locked():
		mutex.release()     #Equivalent au mutex unlock

def Rd_nb(name):
	global Ts
	if name in Ts:
		return Ts[name]
	else:
		return

def In_nb(name):
	global Ts
	valRetour = Rd_nb(name)
	if name in Ts.keys():
		del Ts[name]
		return valRetour
	return None

def Rd_mt(name):
	global Ts
	if name in Ts:
		p.retValue = Ts[name]
		return Ts[name]
	else:
		mutex.acquire()     #equivalent au mutex lock en c
		p.retValue = Ts[name]
		return Rd_mt(name)

def In_mt(name):
	global Ts
	if name in Ts:
		valRetour = Rd(name)
		del Ts[name]
		return valRetour
	else:
		mutex.acquire()     #equivalent au mutex lock en c
		return In_mt(name)

def Rd(name):
	global nb_threads
	nb_threads += 1
	nom_thread = 'rd_' + str(nb_threads)
	_thread.start_new_thread ( Rd_mt, (name,))

def In(name):
	global nb_threads
	nb_threads += 1
	nom_thread = 'in_' + str(nb_threads)
	_thread.start_new_thread ( In_mt, (name,))

def printTs():
	global Ts
	for k,v in Ts.items():
		print(k, v)
