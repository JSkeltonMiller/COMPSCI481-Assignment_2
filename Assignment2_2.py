import math
import operator
dict1 = {}

def findTriples(n):  # make algortithm to find triples
    triplesList = []
    for c in range(int(1), int(n) + 1):  # error here--n read as string
        for a in range(1, c):
            for b in range(1, a + 1):
                if a * a + b * b == c * c:
                    triplesList.append((a, b, c))
    return triplesList


def filterTriples(triplesList):  # remove triples that have a common factor greater than one
    newList = []
    for trip in triplesList:
        a = trip[0]
        b = trip[1]
        c = trip[2]

        no_common_var = True
        for test in range(2, b):
            if a % test == 0 and b % test == 0 and c % test == 0:
                no_common_var = False

        if no_common_var:
            newList.append(trip)
    return newList



def sortTriples(newList):  # make a dictionary with each triple as a tuple matched with the area
    for trl in newList:
        a = int(trl[0])
        b = int(trl[1])
        c = int(trl[2])
        test1 = str(a) +','+ str(b) +','+ str(c)
        dict1[test1] = a * b * .5

    sorted_dict1 = sorted(dict1.items(), key =operator.itemgetter(0), reverse = True)
    return sorted_dict1


def main():
    print ("Please enter an integer representing maximum side length: ")
    n = raw_input()  # user input
    tripList1 = findTriples(n)
    tripList2 = filterTriples(tripList1)
    for triplet in sortTriples(tripList2):
        print triplet[0]


# use other functions to generate, filter, and sort lists
main()

