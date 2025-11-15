#!/usr/bin/env python3
# Created By: Christopher El-Murr
# Date: 11 14, 2025
# This program uses ses a do..while loop calculate the factorial of the number


def main():
    # get user input and try to convert to an int
    user_num = input("Please enter a positive integer: ")
    try:
        user_num = int(user_num)
        if user_num <= 0:
            print("Please enter a positive integer.")
        else:
            # initialize counter and factorial answer
            counter = 0
            factorial_answer = 1

            # Calculate the factorial of the user input
            while True:
                counter = counter + 1
                factorial_answer = factorial_answer * counter

                # break loop if counter is greater than or equal to user_num
                if counter >= user_num:
                    break

            # display output
            print("The factorial of", user_num, "is", factorial_answer)

    except ValueError:
        print(user_num, "Please enter a valid integer")

    # display thanks for playing at the end of the program
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
