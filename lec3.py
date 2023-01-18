import random
r = random.randint(1,20)

while(True):
	i = int(input())
	if(i<r):
		print("wrong guess, enter a greater number")
	elif(i>r):
		print("wrong guess,enter a smaller number")
	else:
		print("congrats, you've guessed the right number")
		break;	