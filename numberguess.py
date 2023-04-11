import random
num = random.randint(1, 100)
guesses = 0
max_guesses = 10

while True:
    try:
        number = int(input("Guess what number I am thinking of between 1 and 100: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue
    
    if number == num:
        print("Congratulations you guessed the correct number in", guesses, "guesses.")
        break
    elif number > num:
        print("Your guess was a little too high, would you like to take another guess?")
    else:
        print("Your guess was a little too low, would you like to guess again?")
    
    
    guesses += 1
    guess_left = max_guesses - guesses
    print("You have", guess_left, "guesses left.")
    if guesses == max_guesses:
        print("You ran out of guesses")
        break
    
    quit = input("Do you want to quit? Y/N ")
    if quit.upper() == 'Y':
        print("The number was", num)
        break
