from gameFunctions import gameVars

# what are you trying to compare inside this function?
# you will need to pass those things in as arguments
# inside the round brackets
def comparechoices():

	if gameVars.player == "quit":
			exit()
		elif gameVars.computer == gameVars.player:
			print("tie! no one wins, play again")
	
		elif gameVars.player.lower() == "rock":
			if gameVars.computer == "paper":
				print("You Lose!", gameVars.computer, "covers", gameVars.player, "\n")
				gameVars.player_lives = gameVars.player_lives - 1
			else:q
				print("You Win!", gameVars.player, "smashes", gameVars.computer, "\n")
				gameVars.computer_lives = gameVars.computer_lives - 1

		elif gameVars.player.lower() == "paper":
			if gameVars.computer == "scissors":
				print("You Lose!", gameVars.computer, "cuts", gameVars.player, "\n")
			else:
				print("You Win!", gameVars.player, "smashes", gameVars.computer, "\n")

		elif gameVars.player.lower() == "scissors":
			if gameVars.computer == "rock":
				print("You Lose!", gameVars.computer, "smashes", gameVars.player, "\n")
			else:
				print("You Win!", gameVars.player, "cuts", gameVars.computer, "\n")

		else:
			print("That's not a valid choice, try again")
