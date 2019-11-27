"""

Logic for "Finish the Phrase" game.
Some ideas/points for implementation:
- Put all movie lines into an array and randomly select which to ask the user 
- User will input a string, lowercase everything in the string.

"""

from graphics import *
import sys
from random import randrange

def read_file():

	window = GraphWin("Finish the Phrase", 400, 400)
	window.setBackground("pink")
	
	entry_text = Entry(Point(200, 150), 50)
	entry_text.draw(window)	
		
	# Open the input file and put into an array
	num_lines = 21
	with open("input.txt") as input_file:
		lines = input_file.readlines()
	content = [x.strip() for x in lines]

	# Randomly select a movie phrase
	rand = randrange(20)
	selected_phrase = content[rand]
	split_phrase = selected_phrase.split(" ")	
	answer = split_phrase[-1] # The answer is the last element 

	intro = Text(Point(200, 20), "Finish the movie phrase. Enter 'exit' to quit.\n Click anywhere on the window to submit text.")
	intro.draw(window)
	prompt = Text(Point(200, 60), "The movie phrase is: ")	
	prompt.draw(window)
	
	new = split_phrase[:-1]
	string = " ".join(new)
	message = Text(Point(190, 80), string)
	message.draw(window)
	
	exit_text = Text(Point(200, 190), "Click here to submit text.")
	exit_text.draw(window)

	count = 3
	for i in range(3):
		count = count - 1
		window.getMouse() # Says done writing text
		user_input = entry_text.getText()
		print("User entered: ", user_input)
		if (user_input.lower() == answer.lower()):
			print("CORRECT!")
			break
		elif (user_input.lower() == "exit"):
			break
		else:
			print("WRONG! You have", count, "more tries.")		
	
		
	window.close()
	
read_file()
