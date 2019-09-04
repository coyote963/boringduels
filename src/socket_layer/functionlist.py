from socket_layer.helper import send_to_socket, is_current_session_ign, is_current_session_steam
def packet_type_filter(packet_type):
	'''A decorator filter for handling different packet types. function doesn't called if it doesn't match the packet_type. '''
	def wrapdecorator(func):
		def wrapfunction(*args, **kwargs):
			if packet_type == args[0].get('option'):
				func(*args, **kwargs)
		return wrapfunction
	return wrapdecorator

def join_filter(func):
	'''a decorator filter for handling a player joining. Function doesn't get called if packet doesn't contain a join message'''
	def wrapfunction(*args, **kwargs):
		if 'Chat' == args[0].get('option') and " has joined " in args[0].get('content') and ":" not in args[0].get('content'):
			func(*args, **kwargs)
	return wrapfunction

@packet_type_filter("Chat")
def requestinfo(item, playerq, **kwargs):
	if "info" in item.get('content'):
		send_to_socket(kwargs.get('gamesocket'), "/info")

@join_filter
@packet_type_filter("Chat")
def onplayerjoin(item, playerq, **kwargs):
	'''a function to handle a player joining'''
	user = item.get('content').split(" has joined ")[0]
	send_to_socket(kwargs.get('gamesocket'), "/steam " + user)

def echo (item, playerq, **kwargs):
	'''A function for printing a received packet'''
	for k in item:
		print(str(k) + " : " + str(item.get(k)))
	print("\n")

@packet_type_filter("Chat")
def addbot(item, playerq, **kwargs):
	'''A function that adds a number of bots to the team whenever someone sends a chat message'''
	if "add bots" in item.get('content'):
		send_to_socket(kwargs.get('gamesocket'), "/addbot red")
		send_to_socket(kwargs.get('gamesocket'), "/addbot blue")

@packet_type_filter("Steam ID")
def onsteam(item, playerq, **kwargs):
	print("REACHED HERE")
	if is_current_session_steam(item['steamid'], playerq):
		print("I need to update the database with the new ign")
	else:
		if (is_current_session_ign(item['steamid'], playerq)):
			print("First time user registering, I need to update the database")
		else : 
			print("Unauthorized, kicking")

