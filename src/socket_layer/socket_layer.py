import socket
import configparser
from socket_layer.blocksplit import blocksplit
from collections import deque
from threading import Thread, Event
# this will start a multithreaded process. One will fetch from game, 
# append into a queue, one will consume from the queue and make database calls, 
# finally session manager will take care of the session

# helper function to send non-newline string to the socket properly
def send_to_socket(socket, message):
	message = message + '\n'
	socket.send(message.encode('utf-8'))

# main parent function
def start(pq):
	q = deque()
	e = Event()
	e.wait
	producer = Thread(target = read_from_stream, args=(q, e))
	producer.setDaemon(True)
	producer.start()

	consumer = Thread(target = consume_block, args=( q, e))
	consumer.setDaemon(True)
	consumer.start()
		
def consume_block(q, e):
	
	while (True):
		e.wait()
		while (len(q) > 0):
			print(q.pop())
		e.clear()
		
def read_from_stream(q, e):

	config = configparser.ConfigParser()
	config.read('config.ini')
	host = config['server']['ip_address'] 
	port = int(config['server']['rcon_port'])

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((host, port))
		login = '/rcon ' + config['server']['rcon_password'] 
		send_to_socket(s, login)
		while (True):
			data = s.recv(1024)
			block = blocksplit(data)
			q.append(block)
			e.set()

