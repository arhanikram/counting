from builtins import int
from math import sqrt


ENDING_VALUE = 0


def count_postive_numbers():
    """
    -------------------------------------------------------
    Counts the number of positive numbers entered by the user
    -------------------------------------------------------
    Preconditions:
        num - the integer the user enters (int >= 0)
    Postconditions:
        returns
        count - the amount of positive integers entered (int >= 0) 
    -------------------------------------------------------
    """
    count = 0
    num = -1
    while num != ENDING_VALUE:
        num = int(input("Enter a positive number: "))
        if num > 0:
            count = count + 1
        else:
            count = count

    return count


def perfect_square(num):
    """
    -------------------------------------------------------
    Counts the number of positive numbers entered by the user
    -------------------------------------------------------
    Preconditions:
        num - the integer the user enters (int >= 0)
    Postconditions:
        returns
        count - the amount of positive integers entered (int >= 0) 
    -------------------------------------------------------
    """
    values = []
    n = 0
    while n != num:
        squared = n * n
        if 1 <= squared < num:
            values.append(squared)
        n = n + 1
    return values


def is_prime(num):
    """
    -------------------------------------------------------
    Calculates and displays whether an integer is prime or not
    -------------------------------------------------------
    Preconditions:
        num - the integer whose prime status needs to be found (int)
    Postconditions:
        returns
        status - returns either true or false 
    -------------------------------------------------------
    """
    status = False
    if num < 1:
        while num < 1:
            num = int(input("Invalid entry please enter another number: "))
            status = True
            divisor = 2
            # all even numbers are not prime
            square_root = sqrt(num)
            while divisor <= square_root and status == True:
                if num % divisor == 0:
                    status = False
                divisor += 1
    elif num > 1:
        status = True
        divisor = 2
        # all even numbers are not prime
        square_root = sqrt(num)
        while divisor <= square_root and status == True:
            if num % divisor == 0:
                status = False
            divisor += 1

    else:
        status = False
    return status


def win_game(output):
    """
    -------------------------------------------------------
    Asks a user to input a series of strings
    -------------------------------------------------------
    Preconditions:
        output - the string(s) the user will enter (red/green)
    Postconditions:
        returns
        winning_count - returns whichever colour has more strings
    -------------------------------------------------------
    """
    values = []
    red_count = 0
    green_count = 0
    while output != "":
        output = input("Choose a colour ")
        values.append(output)
        if output == "red":
            red_count = red_count + 1
        elif output == "green":
            green_count = green_count + 1

    return red_count, green_count
