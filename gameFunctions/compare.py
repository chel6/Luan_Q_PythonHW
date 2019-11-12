from random import randint
from gameFunctions import compare, winlose, gameVars
# what are you trying to compare inside this function?
# you will need to pass those things in as arguments
# inside the round brackets
def comparechoices(computer, player):

	if gameVars.player == "quit":
		exit()

	elif gameVars.computer == gameVars.player:
		print("tie! no one wins, play again~ (ง •̀_•́)ง ")
	elif gameVars.player != gameVars.computer:

		if gameVars.player == "rock":
			if gameVars.computer == "paper":
				print("You Lose! ...(｡•ˇ‸ˇ•｡) ... ", gameVars.computer, "covers", gameVars.player, "\n")
				gameVars.player_lives = gameVars.player_lives - 1
			else:
				print("You Win! (੭≧▽≦)੭ ", gameVars.player, "smashes", gameVars.computer, "\n")
				gameVars.computer_lives = gameVars.computer_lives - 1

		elif gameVars.player == "paper":
			if gameVars.computer == "scissors":
				print("You Lose! ...(｡•ˇ‸ˇ•｡) ...", gameVars.computer, "cuts", gameVars.player, "\n")
			else:
				print("You Win! (੭≧▽≦)੭ ", gameVars.player, "smashes", gameVars.computer, "\n")

		elif gameVars.player == "scissors":
			if gameVars.computer == "rock":
				print("You Lose! ...(｡•ˇ‸ˇ•｡) ... ", gameVars.computer, "smashes", gameVars.player, "\n")
			else:
				print("You Win! (੭≧▽≦)੭ ", gameVars.player, "cuts", gameVars.computer, "\n")

	else:
		print("That's not a valid choice, try again (๑>◡<๑) ")


	gameVars.player = False
	gameVars.computer = gameVars.choices[randint(0,2)]