from socket_layer.blocksplit import blocksplit
from collections import deque
from threading import Thread, Event
from socket_layer.functionlist import echo, addbot, onplayerjoin, requestinfo
from socket_layer.helper import create_socket
# this will start a multithreaded process. One will fetch from game, 
# append into a queue, one will consume from the queue and make database calls, 
# finally session manager will take care of the session

def start(pq):
	'''# main parent function'''
	q = deque()
	e = Event()
	s = create_socket()
	#start the producer, reading from stream
	producer = Thread(target = read_from_stream, args=(q, e,s))
	producer.setDaemon(True)
	producer.start()

	#start the consumer, popping from the q
	consumer = Thread(target = consume_block, args=( q, e, [ addbot, onplayerjoin, requestinfo], pq, s))
	consumer.setDaemon(True)
	consumer.start()
		
def consume_block(q, e, functionlist, pq, s):
	'''process to call all the functions in @param functionlist and on each of the elements q.
	Blocks if there is nothing to consume'''
	while (True):
		e.wait()
		while (len(q) > 0):
			item = q.pop()
			for function_element in functionlist:
				function_element(item, pq, gamesocket = s, playerqueue = q)
		e.clear()
		
def read_from_stream(q, e, s):
	'''process to read from a socket and place them into a queue. Calls blocksplit to index the data'''
	while (True):
		data = s.recv(4096)
		block = blocksplit(data)
		# concatenate the two deques
		q += block
		e.set()
