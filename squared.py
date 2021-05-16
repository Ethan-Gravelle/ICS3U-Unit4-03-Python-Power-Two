#!/usr/bin/env python3

# Created by: Ethan Gravelle
# Created on: May 15, 2020
# This program calculates the squares of all numbers up to the user input.

def main():
    # This program calculates the squares of all numbers up to the user input.
    counter = 0
    # input
    print("\n", end="")
    integer = input("Enter a positive integer: ")
    print("")
    # process & output
    try:
        positive_integer = int(integer)
        if positive_integer > 0:
            for counter in range(positive_integer):
                total = counter * counter
                print("{0}² = {1}".format(counter, total))
        else:
            print("Sorry {0} is not a valid input.".format(positive_integer))
    except Exception:
        print("{0} is not a valid input.".format(integer))

    print("\nDone.")


if __name__ == "__main__":
    main()
