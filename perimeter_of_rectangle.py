#!/usr/bin/env python3

# Created by: Euel Yirga
# Created on: Oct 2019
# This program uses user defined functions


def calculate_perimeter(length, width):

    perimeter = 2 * (length + width)

    print("The perimeter is {0} cm".format(perimeter))


def main():

    length_from_user = int(input("Enter the length of a rectangle (cm): "))
    width_from_user = int(input("Enter the width of a rectangle (cm): "))
    print("")

    calculate_perimeter(length_from_user, width_from_user)


if __name__ == "__main__":
    main()
