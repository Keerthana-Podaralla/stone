import random
l=["rock","scissor","papper"]
k = 0
c = 0

while True:
	u=input("enter rock or scissor or papper")
	if u == 'n':
		print("game over")	
		quit()
	c=random.choice(l)
	if u == c:
		print("tie")
	elif u == "rock" and c == "scissor":
		print("user has won")
		k = k +1
	elif u == "scissor" and c == "papper":
		print("user has won")
		k = k +1
	elif u == "papper" and c == "scissor":
		print("comp has won")
		k = k +1
	elif u == "rock" and c == "scissor":
		print("user has won")
		c = c +1
	elif u == "scissor"and c == "papper":
		print("user has won")
		c = c +1
	elif u == "papper" and c == "scissor":
		print("comp has won") 
		c = c +1