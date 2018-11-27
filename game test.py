# Python Text Adventure
# Jacob Drasher

# import allows to grab commands rather than having to hard code them
import cmd # helps use a command line
import textwrap # wrap text around in a console, makes things pretty
import sys # imports system functions
import os # imports operating system functions
import time # time related functions (counter, sleep)
import random # equivalent to rolling a dice

screen_width = 100

# Player Setup
class player: # class creates objects
	def __init__(self):
		self.name = ''
		self.background = ''
		self.hp = 0
		self.status_effects = [] #empty array
		self.location = 'start'
		self.game_over = False # defining whether the player won the game or not.
myPlayer = player()

# Title Screen 
def title_screen_selections():
	option = input("> ")
	if option.lower() == ("play"):
		start_game() # placeholder text for now
	elif option.lower() == ("control"):
		control_menu()  
	elif option.lower() == ("quit"):
		sys.exit() # comes from the sys command we imported
	while option.lower() not in ['play', 'help', 'quit']: # not in will look for these inputs by the user, if these inputs are not selected it will continue looping until they are
		print("Please enter a valid command.")
		option = input("> ")
		if option.lower() == ("play"):
		start_game() # placeholder for now
		elif option.lower() == ("control"):
		help_menu()
		elif option.lower() == ("quit"):
		sys.exit()

# This is what title_screen() at the bottom calls #
def title_screen():
	os.system('clear') # types clear into command prompt automatically, makes a clean title screen to start with.
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	print('~ Welcome to the Doors of Mysteries Text Based Adventure Game'   )
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	print('                     ~    Play   ~                              ')
	print('                     ~  Control  ~                              ')
	print('                     ~    Quit   ~                              ')
	title_screen_selections() # calls the title_screen_selections function above
# this is what the user/player is going to see

def help_menu():
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	print('~                 This is the control menu                  ~')
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	print('- In order to move, use: up, down, left, and right ')
	print('- In order to do a specific command you must type it out. ')
	print('- Use "examine" to inspect something ')
	title_screen_selections()
# The help/control menu the player is going to see

# Visual of the player map
"""
 a1 
-------------
|  |  |  |  |  a4
-------------
-------------
|  |  |  |  |  b4
-------------
-------------
|  |  |  |  |  c4
-------------
-------------
|  |  |  |  |  d4
-------------
"""

# constant variables # what the person will type in order to see these variables
ZoneName = ''
Description = "description" # description of the location
examination = "examine" # what will be said when the player examines a room
Solved = False
UP = 'up', 'north' # these help the player move around the map
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'


# brackets dicate that this is a dictionary
# Will showcase whether the player has sovled the puzzle/room correctly
# can use this do many things 
solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
				 'b1': False, 'b2': False, 'b3': False, 'b4': False,
				 'c1': False, 'c2': False, 'c3': False, 'c4': False,
				 'd1': False, 'd2': False, 'd3': False, 'd4': False,
				} 				   
# solved grid systems

# map is a command in python, have to call the map 'zonemap'
# dictonary of all the zones within the map
zonemap = {
	'a1': { # creating a unique zone for each grid on the map.
		ZoneName: "Top Floor Room #1",
		Description = "description" 
		Examination = "examine" # extra detail to reveal to the player
		Solved = False
		UP = '', 
		DOWN = 'b1',		
		LEFT = '',
		RIGHT = 'a2',
	},
		'a2': { # creating a unique zone for each grid on the map.
		ZoneName: "Top Floor Room #2",
		Description = "description" 
		Examination = "examine" 
		Solved = False
		UP = '',
		DOWN = 'b2',
		LEFT = 'a1',
		RIGHT = 'a3',
	},
		'a3': { # creating a unique zone for each grid on the map.
		ZoneName: "Top Floor Room #3",
		Description = "description" 
		Examination = "examine" 
		Solved = False
		UP = '',
		DOWN = 'b3',
		LEFT = 'a2',
		RIGHT = 'a4',
	},
		'a4': { # creating a unique zone for each grid on the map.
		ZoneName: "Top Floor Room #4",
		Description = "description" 
		Examination = "examine" 
		Solved = False
		UP = '',
		DOWN = 'b4',
		LEFT = 'a3',
		RIGHT = '',
	},
		'b1': { # creating a unique zone for each grid on the map.
		ZoneName: "Upper Floor Room #1",
		Description = "description" 
		Examination = "examine" 
		Solved = False
		UP = 'a1', 
		DOWN = 'c1',
		LEFT = '',
		RIGHT = 'b2',
	},
		'b2': { # creating a unique zone for each grid on the map.
		ZoneName: "Upper Floor Room #2 (starting room)",
		Description = "Pitch black, cold room", 
		Examination = "You find yourself awake within a room that is impossible to see in./nYou are unaware on how you got here." 
		Solved = False
		UP = 'a2',
		DOWN = 'c2',
		LEFT = 'b1',
		RIGHT = 'b3',
	},
		'b3': { # creating a unique zone for each grid on the map.
		ZoneName: "Upper Floor Room #3",
		Description = "description" 
		Examination = "examine" 
		Solved = False
		UP = 'a3', 
		DOWN = 'c3',
		LEFT = 'b2',
		RIGHT = 'b4',
	},
		'b4': { # creating a unique zone for each grid on the map.
		ZoneName: "Upper Floor Room #4",
		Description = "description" 
		Examination = "examine" 
		Solved = False
		UP = 'a4',
		DOWN = 'c4',
		LEFT = 'b3',
		RIGHT = '',
	},
		'c1': { # creating a unique zone for each grid on the map.
		ZoneName: "Lower Floor Room #1",
		Description = "description" 
		Examination = "examine" 
		Solved = False
		UP = 'b1',
		DOWN = 'd1',
		LEFT = '',
		RIGHT = 'c2',
	},
		'c2': { # creating a unique zone for each grid on the map.
		ZoneName: "Lower Floor Room #2",
		Description = "description" 
		Examination = "examine" 
		Solved = False
		UP = 'b2',
		DOWN = 'd2',
		LEFT = 'c1',
		RIGHT = 'c3',
	},
		'c3': { # creating a unique zone for each grid on the map.
		ZoneName: "Lower Floor Room #3",
		Description = "description" 
		Examination = "examine" 
		Solved = False
		UP = 'b3', 
		DOWN = 'd3',
		LEFT = 'c2',
		RIGHT = 'c4',
	},
		'c4': { # creating a unique zone for each grid on the map.
		ZoneName: "Lower Floor Room #4",
		Description = "description" 
		Examination = "examine" 
		Solved = False
		UP = 'b4',
		DOWN = 'd4',
		LEFT = 'c3',
		RIGHT = '',
	},
		'd1': { # creating a unique zone for each grid on the map.
		ZoneName: "Bottom Floor Room #1",
		Description = "description" 
		Examination = "examine" 
		Solved = False
		UP = 'c1',
		DOWN = '',
		LEFT = '',
		RIGHT = 'd2',
	},
		'd2': { # creating a unique zone for each grid on the map.
		ZoneName: "Bottom Floor Room #2",
		Description = "description" 
		Examination = "examine" 
		Solved = False
		UP = 'c2',
		DOWN = '',
		LEFT = 'd1',
		RIGHT = 'd3',
	},
		'd3': { # creating a unique zone for each grid on the map.
		ZoneName: "Bottom Floor Room #3",
		Description = "description" 
		Examination = "examine" 
		Solved = False
		UP = 'c3', 
		DOWN = '',
		LEFT = 'd2',
		RIGHT = 'd4',
	},
		'd4': { # creating a unique zone for each grid on the map.
		ZoneName: "Bottom Floor Room #4",
		Description = "description" 
		Examination = "examine" 
		Solved = False
		UP = 'c4', 
		DOWN = '',
		LEFT = 'd3',
		RIGHT = '',
	},
}

# Game Interactivity
def print_location(): # makes a pretty picture of where the player is
	print('\n' + ('#' * (4 + len(myPlayer.location))))
	print('# ' + myPlayer.location.upper() + ' #')
	print('# ' + zonemap[myPlayer.position][Description] + ' #') # grabs the description of the player's location
	print('\n' + ('#' * (4 + len(myPlayer.location))))
# visual example of the above code^^^
#########
# APPLE #
#########

def prompt(): # prompts the player on what type of move they will make
	print("\n" + "============================")
	print("what would you like to do?")
	action = input("> ")
	acceptable_actions = ['move','go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
	# acceptptable_actions are a list of good actions to do, 
	# if they player does not choose one of these, the player will be forced to choose one.
	while action.lower() not in acceptable_actions
		print("Unknown action, try again.\n")
		action = input("> ")
	if action.lower() == 'quit':
		sys.exit()
	elif action.lower() in ['move', 'go', 'travel', 'walk']:
		player_move(action.lower())
	elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
		player_examine(action.lower())
	# what the player will be interacting with the most
	# where the player is prompt to do everything

def player_move(myAction):
	ask = "Where would you like to move to?\n"
	destination = input(ask) # takes the input the person gives after ask to move them to their destination
	if destination in ['up', 'north']:
		destination = zonemap[myPlayer.location][UP]
		movement_handler(destination)
	elif destination in ['left', 'west']:
		destination = zonemap[myPlayer.location][LEFT]
		movement_handler(destination)
	elif destination in ['east', 'right']:
		destination = zonemap[myPlayer.location][RIGHT]
		movement_handler(destination)
	elif destination in ['south', 'down']:
		destination = zonemap[myPlayer.location][DOWN]
		movement_handler(destination)
	
def movement_handler(destination):
	print("\n" + "You have moed to the " + destination + ".")
	myPlayer.location = destination
	print_location()

def player_examine(action):
	if zonemap[myPlayer.location][SOLVED]: # assumes automatically true
		print("You have already exhausted this zone.")
	else:
		print("You can trigger puzzle/event here.")

# Game Functionality
def start_game(): 
	return

def main_game_loop():
	while myPlayer.game_over is False: # IMPORTANT this is what makes the game work
		prompt()
		# here handle if puzzles have been solved, enemy/obstacle defeated, exploration check, etc.

def setup_game()
	os.system('clear')

	# Getting the user's name
	question1 = "Hello, what's your name?\n"
	for character in question1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	# this is saying for each character in question1, that the program will write it out, 
	# flush it out, and then put a time delay on it. It gives a natural reading effect.
	player_name = input("> ")
	myPlayer.name = player_name

	question2 = "Now, which of these best describe who you are?\n"
	questions2extra = "(You can be any of the following: olympic swimmer, nature lover, or someone who can handle the heat)"
	for character in question2:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	for character in question2extra:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.01)
	player_background = input("> ")
	valid_backgrounds = ['olympic swimmer', 'nature lover', 'someone who can handle the heat']
	if player_background.lower() in valid_backgrounds:
		myPlayer.background = player_background
		print("You are now a " + player_job + "!\n")
	while player_background.lower() not in valid_backgrounds:
		player_background = input("> ")
		if player_background.lower() in valid_backgrounds:
			myPlayer.background = player_background
			print("You are now a " + player_job + "!\n")

# Player stats
if myPlayer.background is 'olympic simmwer':
	self.hp = 100
elif myPlayer.background is 'nature lover':
	self.hp = 70
elif myPlayer.background is 'someone who can handle the heat':
	self.hp = 80

# Introduction for the player
	question3 = "Welcome, " + player_name + " the " + player_background ".\n"
	for character in question1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)


title_screen() # intializes the game, calls the title screen.




