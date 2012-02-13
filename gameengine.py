class Game(object):
	"""The Controller for the game. Handle command line input and naviagates the user through the map"""
	def __init__(self):
		
		current_room = MainRoom()

		command = None

		while(command != "exit"):
			
			print "Current Room:", current_room.title
			print current_room.description

			if current_room.north != None:
				print "Enter N to go North to the %s" % current_room.north.title

			if current_room.south != None:
				print "Enter S to go South"
			
			if current_room.east != None:
				print "Enter E to go East"

			if current_room.west != None:
				print "Enter W to go West"

			command = raw_input('> ')

			if command == "N" and current_room.north != None:
				current_room = current_room.north
			else:
				print "I'm sorry, but I do not understand that command"

class Room(object):
	
	north = None
	south = None
	east = None
	west = None

	title = "Generic Room"
	description = "You have entered a very plain looking room."

	def __init__(self):
		pass

class MainRoom(Room):
	def __init__(self):
		self.north = LivingRoom()

class LivingRoom(Room):
	def __init__(self):
		self.title = "Living Room"