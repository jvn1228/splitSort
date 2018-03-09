#sorting method attempt
#also need to put in negative numbers, duplicates
import math
import time

def splitSort(array, n = -1):   
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
        sortedList += splitSort(lessThan, (middle/2))
    if len(greaterThan) < 2:
        sortedList += greaterThan
    else:
        sortedList += splitSort(greaterThan, middle + (middle/2))
    
    return sortedList
          
def findMax(array):
    currentMax = array[0]
    for i in range(1,len(array)):
        if array[i] > currentMax:
            currentMax = array[i]
    return currentMax

#gimmeList = [34,35]
gimmeList = [1,9,56,322,4,300,17,74,1024,34561,17893,642, 124, 25309, 4875, 34, 21, 123523, 412390582308957, 35, 12, 141,7465, 3457, 86, 65.124, .0123, .00142]
initialTime = time.time()
sortedList = splitSort(gimmeList)
finalTime = time.time()-initialTime
print(sortedList)
print("Took %f seconds" % (finalTime))