import random
import sys
import os

# user rolls a dice
# if number is match - win else try again

def clear_screen():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def welcome():
	clear_screen()

	print("""
###############

Welcome to Roll The Dice

The game is simple, a number will be picked at random between 1 and 6

you will roll a dice and if your number matches the random number

you win!

you will get 3 rolls

type 'quit' at anytime to exit

###############
		""")
	print('')
	start = input("press enter/return to begin or type 'quit' to exit\n>").lower()
	if start == 'quit':
		quit()
	else:
		return True

def quit():
	clear_screen()
	print("""
###############

Thanks for playing!

Created by Samuel Catchpole-Radford
https://github.com/samuelradford


###############
		""")
	sys.exit()

def draw(guesses):
	clear_screen()

	print("\nGuesses so far: {}/3\n".format(len(guesses)))
	print("So far you have rolled: ", end='')
	for guess in guesses:
		print(guess, end=' ')
	print('\n')

def play(finished):
	clear_screen()
	random_num = random.randint(1, 6)
	guesses = []

	while True:

		draw(guesses)
		roll_the_dice = input("Press enter/return to roll\n>")
		if roll_the_dice == 'quit':
			quit()

		user_roll = random.randint(1, 6)

		if user_roll == random_num:
			clear_screen()
			print("\n***** YOU WIN! *****\n")
			print("You rolled a: {}\n".format(user_roll))
			print("The random number was: {}\n".format(random_num))
			finished = True
		else:
			guesses.append(user_roll)
			if len(guesses) == 3:
				clear_screen()
				print("\n***** YOU LOST! *****\n")
				print("You rolled: {}\n".format(guesses))
				print("The random number was: {}\n".format(random_num))
				finished = True
		if finished:
			play_again = input("Do you want to play again? Y/n ")
			if play_again != 'n':
				play(finished=False)
			else:
				quit()



finished = False

welcome()
play(finished)









