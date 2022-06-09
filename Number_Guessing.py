number = 22
attempt = 0

while True:
    attempt += 1
    
    guess = int(input("Guess the number: "))
    
    if(guess > number):
        print("Your guess is too high!")
    
    elif(guess < number):
        print("Your guess is too low!")

    else:
        print(f"You guessed it right in {attempt} attempts!")
        break
    