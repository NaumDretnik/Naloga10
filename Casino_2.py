
import random

print("Welcome to the Lucky Number!")

def main():

    for money_maker in range(5):
        money_maker = random.randint(1, 50)

        lucky_number = int(raw_input("Pick a number between 1 and 50: "))

        if lucky_number == money_maker:
            print("Congratulations! You have won an unlimited supply of cocoa!")
            break
        else:
            print("Sorry, your guess %s was wrong.") % (lucky_number)


main()

print("Thank you for playing. Hope to see you again.")
