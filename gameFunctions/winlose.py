from random import randint
from gameFunctions import winlose, gameVars

# define a python function that takes an argument
def winorlose(status): 
	# status will be either won or lost - you're passing this in as an argument
	print("called win or lose")
	print("************************")

	print("You", status + "! Would you like to play again?")

	choice = input("Y / N: ")
	print(choice)

	if (choice is "N") or (choice is "n"):
		print("You chose to quit.")
		exit()

	elif (choice is "Y") or (choice is "y"):
		# reset the game so that we can start all over again
		# global player_lives
		# global computer_lives
		# global player
		# global computer
		# global choices

		# this will break, currently - we will fix this next class
		gameVars.player_lives = 1
		gameVars.computer_lives = 1
		gameVars.total_lives = 1
		gameVars.player = False
		gameVars.computer = gameVars.choices[randint(0,2)]
	
	else:
		#this is recursion - call a function
		# from inside itself. basically just re-up the choice
		# and force the user to pick yes or no(y or n)
		# use recursion to call winorlose again until we get the right input
		# recuision is just a fancy way to describe calling a function from within itself
		winorlose(status)
		#not a y or n, so make the user pik a valid choce

	# 	# this will break, currently - we will fix this next class
	# 	player_lives = 1
	# 	computer_lives = 1
	# 	player = False
	# 	computer = choices[randint(0,2)]
	
	# else:
	# 	# not a y or n, so make the user pick a valid choice
	# 	print("make a valid choice, Y or N")
	# 	# this is recursion - call a function
	# 	# from inside itself. Basically just re-up the choice
	# 	# and force the user to pick yes or no (y or n)
	# 	winorlose(status)

