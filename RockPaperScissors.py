#Inorder to let computer choose randomly
import random

#Print a welcome statement for users

print('Welcome to Rock-Paper-Scissors! ')
print('-----------------------------------------------------')

#Setup variable to keep track of scores

cPUScore = 0
playerScore = 0
tieScore = 0

#Layout possible combinations as a list
possibleHands = ['Rock', 'Paper', 'Scissors']

#Layout a function to call later to determine who won

def checkForWinner(playerHand, computerHand):
	if(playerHand == 'Rock' and computerHand == 'Paper'):
		print('Sorry, you lost :( ')
		return 'CPU'
	elif(playerHand == 'Rock' and computerHand == 'Scissors'):
		print('Yay! You won! :) ')
		return 'Player'
	elif(playerHand == 'Paper' and computerHand == 'Scissors'):
		print('Sorry, you lost :( ')
		return 'CPU'
	elif(playerHand == 'Paper' and computerHand == 'Rock'):
		print('Yay! You won! :) ')
		return 'Player'
	elif(playerHand == 'Scissors' and computerHand == 'Rock'):
		print('Sorry, you lost :( ')
		return 'CPU'
	elif(playerHand == 'Scissors' and computerHand == 'Paper'):
		print('Yay! You won! :) ')
		return 'Player'
	else:
		print('It\'s a tie. Play again.')
		return 'Tie'
	
	
#Write game logic as a while loop
	
while(playerScore != 3 and cPUScore != 3):
	#Validation loop to validate input
	while True:
		playerHand = input('\nPick a hand. Rock, Paper or Scissors: ')
		if(playerHand == 'Rock' or playerHand == 'Paper' or playerHand == 'Scissors'):
			break
		else:
			print('Invalid input. Try again. ')
	
	#Generate computerHand
	
	computerHand = random.choice(possibleHands)
	
	#Print results
	print('Your Hand: ', playerHand)
	print('CPU Hand: ', computerHand)
	result = checkForWinner(playerHand, computerHand)
	if(result == 'Player'):
		playerScore += 1
	elif(result == 'CPU'):
		cPUScore += 1
	else:
		tieScore += 1
		
	print('Your Score: ', playerScore, 'CPU: ', cPUScore, 'Ties: ', tieScore)
	
	
print('Gameover! Thanks for playing :) ')

