# import the random package so that we can generate a random choice
from random import randint
from gameFunctions import winlose, gameVars

while gameVars.player is False:
	# set player to True
	
	print("************************************")
	print("Computer lives:", gameVars.computer_lives,"/",gameVars.total_lives, "\n")
	print("Player lives:", gameVars.player_lives,"/",gameVars.total_lives, "\n")
	print("Choose your weapon!\n")
	print("************************************")
	
	gameVars.player = input("choose rock, paper or scissors\n")
	gameVars.player = gameVars.player.lower()

	print("computer chose", gameVars.computer_lives, "\n")
	print("player chose", gameVars.player, "\n")


### this is where function should be

### compare need put it here


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

