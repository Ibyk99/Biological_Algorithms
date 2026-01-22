import time # a library needed fo timing functions
import pandas

#import the scripts
from bubbleSort import bubbleSort
from quickSort import quickSort
from selectionSort import selectionSort

#This reads a file...
def readFile(fle):
    f = open(fle, 'r')
    x = f.readlines()
    f.close()
    results = [int(i) for i in x]
    return results


#This can be passed a file to sort and the sort algorithm
def testPerformance(filename,algorithm):
    arr2 = readFile(filename)
    start = time.time()
    if algorithm == quickSort:
         algorithm(arr2,0,len(arr2)-1)
    else:
        algorithm(arr2)
    elapsed =time.time()-start

    #how to print the elapsed time
    print("")
    print("Sorted big container: %s secs" % elapsed)
    for i in range(10):
           print(arr2[i],end=" ")
    print("")
    return elapsed 

#driver code example
for sort_type in [bubbleSort, selectionSort, quickSort]:
    for item in ["random5000", "random20000", "random5000sorted"]:
        print(f"\nSorting using \"{sort_type.__name__}\" and \"{item}.txt\"")
        testPerformance(f"{item}.txt",sort_type)

