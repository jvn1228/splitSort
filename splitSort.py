#sorting method, handles repeats, negatives, floating point
#by Jonathan Nguyen
import math
import time
import random

def splitSort(array):
    #head splitSort function, just takes an array
    #find Repeats and remember them
    [noRepeats, repeatDict] = findRepetitions(array)
    #seperate negative and positive numbers
    arrayNeg = map(lambda x: x*-1, filter(lambda x: x<0, noRepeats))
    arrayPos = filter(lambda x: x>=0, noRepeats)
    #sort the processed lists
    posSortedList = []
    negSortedList = []
    if len(arrayPos) > 0:
        posSortedList = splitSortRecursive(arrayPos)
    if len(arrayNeg) > 0:
        negSortedList = splitSortRecursive(arrayNeg)
        #put negative numbers in appropriate order
        negSortedList = map(lambda x: x*-1, negSortedList)
        negSortedList.reverse()
        #join both lists together
    sortedList = negSortedList + posSortedList
    #make final lists with the repeats
    finalList = []
    for i in range(len(sortedList)):
            finalList.extend([sortedList[i]]*repeatDict[sortedList[i]])
    
    return finalList
    

def splitSortRecursive(array, n = -1):   
    #main recursive function, recursively splits mid point until all numbers are
    #sorted into individual lists, then concatenates all back up
    if n == -1:
        maxVal = float(findMax(array))
        middle = 2**(round(math.log(maxVal/2,2)))
    else:
        middle = n
 
    lessThan = []
    greaterThan = []
    
    for i in range(len(array)):
        if array[i] < middle:
            lessThan.append(array[i])
        else:
            greaterThan.append(array[i])
    
    sortedList = []

    if len(lessThan) < 2:
        sortedList += lessThan
    else:    
        sortedList += splitSortRecursive(lessThan, (middle/2))
    if len(greaterThan) < 2:
        sortedList += greaterThan
    else:
        sortedList += splitSortRecursive(greaterThan, middle + (middle/2))
    
    return sortedList
          
def findMax(array):
    #finds the max of array to determine first split point
    currentMax = array[0]
    for i in range(1,len(array)):
        if array[i] > currentMax:
            currentMax = array[i]
    return currentMax
    
def findRepetitions(array):
    #removes repetitions to be added in after sorting
    repetitions = {}
    noRepeats = []
    for n in array:
        if n not in repetitions:
            repetitions[n] = 1
            noRepeats.append(n)
        else:
            repetitions[n] += 1
    return [noRepeats, repetitions]


def main():
    #test function
    #gimmeList = [34,35]
    #gimmeList = [-5, -12, 0, 124, 24]
    #gimmeList = [5,4,3,2,1]
    gimmeList = [1,9,56,322,4,300,17,74,1024,34561,0, 17893,-53,642, 124, 0, 25309, 4875, -241, 34, 21, 123523, -24.1244, -10, -11, 412390582308957, 0, 35, 12, 141,7465, 123908.234, -123.11235, 7465,3457, 86, 65.124, -12, 12, .0123, .00142, 134, 1235, 12, 124, 39, 210, 0.315, 124, -197, 87, 56, -87, 354, 219, -1, 53,18,936, 219, -2935]
    initialTime = time.time()
    sortedList = splitSort(gimmeList)
    finalTime = time.time()-initialTime
    print(sortedList)
    

if __name__ == "__main__":
    main()