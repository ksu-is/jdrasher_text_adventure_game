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
		self.hp = 0
		self.mp = 0
		self.status_effects = [] #empty array
		self.location = 'start'
player_character = player()

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

def title_screen():
	os.system('clear') # types clear into command prompt automatically, makes a clean title screen to start with.
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	print('~ Welcome to the Doors of Mysteries Text Based Adventure Game'   )
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	print('                     ~    Play   ~                              ')
	print('                     ~  Control  ~                              ')
	print('                     ~    Quit   ~                              ')
	title_screen_selections()
# this is what the user/player is going to see

def help_menu():
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	print('~                 This is the control menu                  ~')
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	print('- In order to move, use: up, down, left, and right ')
	print('- In order to do a specific command you must type it out. ')
	print('- Use "search" to inspect something ')
	title_screen_selections()

def start_game(): # game functionality


# Visual of the player map
"""
 a1 
-------------
|  |  |  |  |  
-------------
-------------
|  |  |  |  |  
-------------
-------------
|  |  |  |  |  
-------------
-------------
|  |  |  |  |  
-------------
"""

# constant variables
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
solved_places = {'a1': False,
} 				   


# map is a command in python, have to call the map 'zonemap'
zonemap =
