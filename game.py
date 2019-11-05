# import the random package so that we can generate a random choice
from random import randint
from gameFunctions import winlose

#set up some variables for player and AI lives
player_lives = 1
computer_lives = 1

# choices is an array => an array is a container that can hold multiple values
# arrays are 0-based ->first entry is 0, 2nd
choices = ["rock", "paper", "scissors"]

# set the computer variable to one of these choices
computer = choices[randint(0, 2)]

# set up the game loop so that we don't have to restart all the time
player = False

# define a python function that takes an argument
def winorlose(status): 
	# status will be either won or lost - you're  passing this in as an argument
	print("called win or lose")
	print("****************************")

	print("You",status, "! Would you like to play again?")

	choice = input("Y / N")
	print(choice)

	if (choice is "N") or (choice is "n"):
		print("You chose to quit.")
		exit()
	elif (choice is "Y") or (choice is "y"):
		#reset the game so that we can start all over again
		global palyer_lives
		global computer_lives
		global player
		global computer
		global choices

		player_lives = 1
		computer_lives = 1
		player = False
		computer = choices[randint(0,2)]

while player is False:
	# set player to True
	
	print("************************************\n\n")
	print("Computer lives:", computer_lives,"/5","\n")
	print("Player lives:", player_lives,"/5","\n")
	print("Choose your weapon!\n\n")
	print("************************************\n\n")
	
	player = input("choose rock, paper or scissors\n")
	player = player.lower()

	print("computer chose", computer, "\n")
	print("player chose", player, "\n")

	if player == "quit":
		exit()
	elif computer == player:
		print("tie! no one wins, play again")
	
	elif player.lower() == "rock":
		if computer == "paper":
			print("You Lose!", computer, "covers", player, "\n")
			player_lives = player_lives - 1
		else:
			print("You Win!", player, "smashes", computer, "\n")
			computer_lives = computer_lives - 1

	elif player.lower() == "paper":
		if computer == "scissors":
			print("You Lose!", computer, "cuts", player, "\n")
		else:
			print("You Win!", player, "smashes", computer, "\n")

	elif player.lower() == "scissors":
		if computer == "rock":
			print("You Lose!", computer, "smashes", player, "\n")
		else:
			print("You Win!", player, "cuts", computer, "\n")

	else:
		print("That's not a valid choice, try again")

	# handle all lives lost for player or AI
	if player_lives is 0:
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

	elif computer_lives is 0:
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
		player = False
		computer = choices[randint(0, 2)]
