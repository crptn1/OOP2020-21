# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: B. Schoen-Phelan
# date: 02-10-2020
# purpose: Lab 2
from typing import List


class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message: str = input("Enter your noun: ")
        print("Originally entered: " + message)

        #
        # Enter your own print statements below:
        #

        # print only first and last of the sentence:
        print("The first and last element of name are:{0}{1}".format(message[0], message[-1])

              )

        # use slice notation:
        print(message[:4])
        print(message[2:])
        print(message[:])

        # escaping a character:
        print('He said "that\'s fantastic\"!')

        # find all a's in the input word and count how many there are:
        print(message.find("a"), 'is the position of the first "a" ')
        print(message.count("a"), "is the amount of \"a\" in the word")

        # replace all occurences of the character a with the - sign
        print(message.replace("a", "-"))
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace():

    def play_with_lists(self):
        message: str = input("Please enter a whole sentence: ")
        print("Originally entered: " + message)

        # hand the input string to a list and print it out:

        my_list: List[str] = list(message.split())
        print(my_list)
        # append a new element to the list and print:
        my_list.append("average")
        print(my_list)

        # remove from the list in 3 ways:
        #my_list.remove("yes")
        del my_list[2]
        my_list.pop(1)


        # check if the word cake is in your input list:
        if -1 == message.find("cake"): print("Cake is not in the input list")
        # reverse the items in the list and print:

        my_list.reverse()
        print(my_list)

        # reverse the list with the slicing trick:
        my_list[::-1]
        print(my_list)

        # print the list 3 times by using multiplication:
        print(my_list*3)


tas = Types_and_Strings()
#tas.play_with_strings()
tas.play_with_lists()
