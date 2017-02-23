import random

def generator():
    print("Welcome to the Lottery generator.")
    lucky_set = []
    usr_num = int(raw_input("Please enter the length of the lottery set you desire: "))

    while True:
        lottery_num = random.randint(1, 30)
        if len(lucky_set) < usr_num:
            if lottery_num not in lucky_set:
                lucky_set.append(lottery_num)
                lucky_set.sort()
        else:
            break

    print("Here are the %r lucky numbers for tonight's draw: %r") % (usr_num, lucky_set)

    with open("loterija.txt", "w") as lottery:
        lottery.write("Here are the %r lucky numbers for tonight's draw:\n%r" % (usr_num, lucky_set))

generator()

