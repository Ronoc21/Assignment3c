# Conor Smith
# Date: 04/14/2021
# Description: Plays a game with user. User attempts to guess a given number

print("Enter the integer for the player to guess.")#Get the number that needs to be guessed
num = int(input())

tries = 1 #how many attempts it has taken
print("Enter your guess.")#player guesses original number
guess = int(input())

while guess > num: #while loop when guess is incorrect
    print("Too high - try again:")
    tries += 1#add 1 to total amount of tries
    guess = int(input())#get new guess
while guess < num:#while loop when guess is incorrect
    print("Too low - try again:")
    tries += 1#add 1 to total number of tries
    guess = int(input())#get another input
if guess == num:#when they get it right
    print("You guessed it in", tries, "tries.")