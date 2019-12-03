'''
Author: James Kang
Description: Basically my thought process is that a bot will be able to solve math equations very fast
With this understand we will create some simple math problems (some harder than other)
and if the "user" is able to solve it within fraction of seconds we can know that
this is infact a bot and not an actual person. Yeet
'''

import random
import string

def main():
	lines = [line.split('\n') for line in open('input.txt')]
	ran = random.randint(0,len(lines) - 1)
	question = lines[ran][0].split(",")
	test = 3
	while(test > 0):
		if(test == 3):
			print("Please answer the following math question ignoring the order of operations, solve from left to right")
		print(question[0])
		u_answer = input()
		a_answer = question[1]
		if(u_answer == a_answer):
			print("You got the right answer! you ain't no bot")
			return;
		else:
			print("hello bot! Please try again", test - 1, "tries remaining tries")
			test -= 1

	print("Sorry we couldn't verify that you were a human :( hopefully you have a better luck next time")



if __name__ == "__main__":
	main()
