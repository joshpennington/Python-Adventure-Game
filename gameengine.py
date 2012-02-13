class Game(object):
	"""The Controller for the game. Handle command line input and naviagates the user through the map"""
	def __init__(self):
		
		main_room = MainRoom()
		living_room = LivingRoom()
		bed_room = BedRoom()
		dining_room = DiningRoom()

		main_room.set_east(living_room)
		main_room.set_south(bed_room)

		living_room.set_west(main_room)
		living_room.set_south(dining_room)

		bed_room.set_north(main_room)
		bed_room.set_east(dining_room)

		dining_room.set_north(living_room)
		dining_room.set_west(bed_room)

		current_room = main_room

		command = None

		while(command != "exit"):
			
			print "Current Room:", current_room.title
			print current_room.description

			if current_room.north != None:
				print "Enter N to go North to the %s" % current_room.north.title

			if current_room.south != None:
				print "Enter S to go South to the %s" % current_room.south.title
			
			if current_room.east != None:
				print "Enter E to go East to the %s" % current_room.east.title

			if current_room.west != None:
				print "Enter W to go West to the %s" % current_room.west.title

			command = raw_input('> ')

			if command == "N" and current_room.north != None:
				current_room = current_room.north
			elif command == "S" and current_room.south != None:
				current_room = current_room.south
			elif command == "E" and current_room.east != None:
				current_room = current_room.east
			elif command == "W" and current_room.west != None:
				current_room = current_room.west
			elif command == "exit":
				pass
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

	def set_north(self, room):
		self.north = room
	
	def set_south(self, room):
		self.south = room
	
	def set_east(self, room):
		self.east = room
	
	def set_west(self, room):
		self.west = room

	def set_rooms(self, n, e, s, w):
		set_north(n)
		set_east(e)
		set_south(s)
		set_west(w)

class MainRoom(Room):
	def __init__(self):
		self.title = "Main Room"
		self.description = "This is the main room"

class LivingRoom(Room):
	def __init__(self):
		self.title = "Living Room"
		self.description = "A room that appears to have a lot of living in it"

class BedRoom(Room):
	def __init__(self):
		self.title = "Bed Room"
		self.description = "A bed in room. Seems pretty self explanitory"

class DiningRoom(Room):
	def __init__(self):
		self.title = "Dining Room"
		self.description = "There is a table and four chairs"