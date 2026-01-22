# Sorting Algorithms  

## Selection Sort  
- Sorted and Unsorted files of same length take the same amount of time to run (0.43 seconds)
- An increase in filesize from 5000 to 20000 causes an increase in time (0.43 seconds to ~7 seconds)

## Bubble Sort
- We see a significant decrease in time between the sorted and unsorted. 
- However, the increase in filesize causes a large change in time, this is because O(N^2) tells us how it scales but does not tell us how long one swap takes in the algorithm so we can't directly compare times between algorithms without first calculating a single swap.

```python
def bubbleSort(arr):
    swapped = True
    n = len(arr)
    x = 0
    # Traverse through all array elements
    while bool(swapped):
    swapped = False
    # Last I elements are already in place
    for j in range(0, n - 1 -x):
    if arr[j] > arr[j + 1]:
    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    swapped = True
    x=x+1
```
Swapped tells us if there's been a swap - if there's not a swap then things in that block are in order so we can move on.

## Quick Sort
- The quickest one here
- Shorter time for sorted vs unsorted and v short time for larger files.



Would it make sense to start the timer before reading the array file to give
an indication of the overall runtime performance?
No - we assume everything is in memory when we start 