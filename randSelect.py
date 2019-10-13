##########################################################################
#
#    Tufts University, Comp 160 randSelect coding assignment  
#    randSelect.py
#    randomized selection
#
#    includes functions provided and function students need to implement
#
##########################################################################

import random


def randSelect(ray, index):
	print ("Looking for value with rank", index, " in the array:\n", ray)
	pivot = random.randint(0,len(ray) - 1)
	newRank, ray = partition(ray, pivot)
	if newRank > index:
		print("Selected", ray[newRank], "as the pivot; its rank is",newRank,"; Thus, we recurse on the left", "\n")
		return randSelect(ray[:newRank], index)
	elif newRank < index:
		print("Selected", ray[newRank], "as the pivot; its rank is", newRank,"; Thus, we recurse on the right", "\n")
		return randSelect(ray[newRank + 1:], index - newRank - 1)
	else:
		print("Selected", ray[newRank], "as the pivot; its rank is", newRank,"; Thus, we recurse on nothing. We are done.")
		return ray[newRank]

def partition(ray, pivot): 
	firstHalf = []
	secondHalf = []

	for element in ray:
		if element < ray[pivot]:
			firstHalf.append(element)
		elif element > ray[pivot]:
			secondHalf.append(element)


	newIndex = len(firstHalf)  
	ray = firstHalf + [ray[pivot]] + secondHalf
	return newIndex, ray