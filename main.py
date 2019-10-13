##########################################################################
#
#    Tufts University, Comp 160 randSelect coding assignment  
#    main.py
#    randomized selection
#
#    simple main to test randSelect
#    NOTE: this main is only for you to test randSelect. We will compile
#          your code against a different main in our autograder directory
#
##########################################################################

from randSelect import randSelect
from randSelect import partition


def main():
	v = [3, 4, 5, 1, 2, 7, 8, 6]
	rankWeWant = 3
	ourNumber = randSelect(v, rankWeWant)
	expectedNumber = sorted(v)[rankWeWant]
	print("Expected ", expectedNumber, " our number ", ourNumber)
	if ourNumber != expectedNumber:
		print("Noooo!")
	else:
		print("Yayy!")


if __name__ == '__main__':
	main()