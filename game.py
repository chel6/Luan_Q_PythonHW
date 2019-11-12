# import the random package so that we can generate a random choice
from random import randint
from gameFunctions import winlose, gameVars

# #set up some variables for player and AI lives
# player_lives = 1
# computer_lives = 1
# total_lives = 1

# # choices is an array => an array is a container that can hold multiple values
# # arrays are 0-based ->first entry is 0, 2nd is 1, 3rd is 2 etc
# choices = ["rock", "paper", "scissors"]

# # set the computer variable to one of these choices (0, 1 or 2)
# computer = choices[randint(0, 2)]

# # set up the game loop so that we don't have to restart all the time
# player = False

# define a python function that takes an argument
# def winorlose(status): 
# 	# status will be either won or lost - you're  passing this in as an argument
# 	print("called win or lose")
# 	print("****************************")

# 	print("You",status, "! Would you like to play again?")

# 	choice = input("Y / N")
# 	print(choice)

# 	if (choice is "N") or (choice is "n"):
# 		print("You chose to quit.")
# 		exit()
# 	elif (choice is "Y") or (choice is "y"):
# 		#reset the game so that we can start all over again
# 		global palyer_lives
# 		global computer_lives
# 		global player
# 		global computer
# 		global choices

# 		player_lives = 1
# 		computer_lives = 1
# 		player = False
# 		computer = choices[randint(0,2)]

while gameVars.player is False:
	# set player to True
	
	print("************************************")
	print("Computer lives:", gameVars.computer_lives,"/",gameVars.total_lives, "\n")
	print("Player lives:", gameVars.player_lives,"/",gameVars.total_lives, "\n")
	print("Choose your weapon!\n")
	print("************************************")
	
	gameVars.player = input("choose rock, paper or scissors\n")
	gameVars.player = gameVars.player.lower()

	print("computer chose", gameVars.computer, "\n")
	print("player chose", gameVars.player, "\n")

	### this is where you would call compare
	
	####end compare stuff

	# handle all lives lost for player or AI
	if gameVars.player_lives is 0:
		winlose.winorlose("lost")
		# print("Out of lives! You suck at this game. Would you like to play again?\n")
		# choice = input("Y / N")
		# print(choice)

		# if (choice is "N") or(choice is "n"):
			# print("You chose to quit.")
			# exit()
		# elif (choice is "Y") or (choice is "y"):
			#reset the game so that we can start all over again
			# player_lives = 5
			# computer_lives = 5
			# player = False
			# computer = choices[randint(0,2)]

	elif gameVars.computer_lives is 0:
		winlose.winorlose("won")
		# print("Cumputer is out of lives! You rock at this game. Would you like to play again?\n")
		# choice = input("Y / N")
		# print(choice)

		# if (choice is "N") or(choice is "n"):
			# print("You chose to quit.")
			# exit()
		# elif (choice is "Y") or (choice is "y"):
			#reset the game so that we can start all over again
			# player_lives = 5
			# computer_lives = 5
			# player = False
			# computer = choices[randint(0,2)]

	else:
	# need to check all of our conditions ager checking for a tie
	
		gameVars.computer = choices[randint(0, 2)]
