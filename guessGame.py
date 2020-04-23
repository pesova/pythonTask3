import random


firstStage = random.randint(1, 10)
secondStage = random.randint(1, 20)
ThirdStage = random.randint(1, 50)

#counts the guesses
guess_count = 0
print('''
Welcome to this game, choose your Stage.
These are the stages:
E --- Easy
M --- Medium
H --- Hard''')


Stages = input("Attention!!, you are to select your stage [E; M; or H]: ").upper()

if Stages == "E":
    guess_limit = 6
    secret_number = firstStage
    print("In this Stage you have between 1 and 10, and you have only 6 guesses")
elif Stages == "M":
    guess_limit = 4
    secret_number = secondStage
    print("In this Stage you have between 1 and 20, and you have only 4 guesses")
else:
    if Stages == "H":
        guess_limit = 3
        secret_number = ThirdStage
        print("In this Stage you have between 1 and 50, and you have only 3 guesses")


# run the game till guess is zero
while guess_count < guess_limit:
    try:
        guess = int(input('guess the correct number: '))
        guess_count += 1
        if guess < secret_number or guess > secret_number:
            print('That was wrong')
        else:
            if guess == secret_number:
                break
    except ValueError:
        print('Enter your guess.')
        continue
if guess == secret_number: # this happens if user guess is right
    guess_count = str(guess_count)
    print('You got it right')
else:
    if guess != secret_number: # if user wrong/exhausted life line
        secret_number = str(secret_number)
        print('Game Over, You guessed all Wrong, The correct guess is ' + secret_number)
