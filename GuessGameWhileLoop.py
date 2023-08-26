guess_count = 0
secret_number = 9
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess number(0-9): "))
    guess_count += 1
    if guess == secret_number:
        print("You win!")
        break
else:
    print("Sorry you failed!")

# else is executed if while loop ends successfully(condition=FALSE) without immediate break
