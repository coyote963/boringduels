import configparser
import socket

def send_to_socket(socket, message):
	'''helper function to send non-newline string to the socket properly'''
	message +=  "\n"
	socket.send(bytes(message, "utf-8"))

def create_socket():
	'''Creates a socket as defined by the config file'''
	config = configparser.ConfigParser()
	config.read('config.ini')
	host = config['server']['ip_address'] 
	port = int(config['server']['rcon_port'])
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	login = '/rcon ' + config['server']['rcon_password'] 
	send_to_socket(s, login)
	return s

def is_current_session_ign(name, playerqueue):
	'''Checks if the current session has a player on the reservation list based off ign'''
	return playerqueue.current_session.man_player.ign == name or playerqueue.current_session.usc_player.ign == name

def is_current_session_steam(steam, playerqueue):
	'''Checks if the current session has a player on the reservation list based off steam'''
	return playerqueue.current_session.man_player.steam_id == steam or playerqueue.current_session.usc_player.steam_id == steam