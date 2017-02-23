import random

def main():
    drzave_v_mesta = {
        "Slovenia": "Ljubljana",
        "Austria": "Vienna",
        "Italy": "Rome",
        "Croatia": "Zagreb",
        "Hungary": "Budapest",
        "Germany": "Berlin",
        "United States": "Washington",
        "North Korea": "Pyongyang",
        "Afghanistan": "Kabul",
        "Albania": "Tirana",
        "Thailand": "Bangkok"
    }

    while True:
        nakljucno_mesto = random.randint(0, 9)
        drzava = drzave_v_mesta.keys()[nakljucno_mesto]
        uganjeno_mesto = raw_input("What is the capital of " + drzava + "? ")

        if preveri(drzava, uganjeno_mesto, drzave_v_mesta) == False:
            break

def preveri(drzava, uganjeno_mesto, drzave_v_mesta):
    dejansko_mesto = drzave_v_mesta[drzava]
    while uganjeno_mesto == dejansko_mesto:
        print("You're right. The capital of " + drzava + " is " + dejansko_mesto + ".")
        return True
    else:
        print("You're wrong. The capital of " + drzava + " is " + dejansko_mesto + ".")
        print("This is the end, my friend...")
        print("__________________________________")
        return False

if __name__ == '__main__':
    main()