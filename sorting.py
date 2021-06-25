# Bubble sort
# Parameters: An array to sort
# Return: A sorted array
def bubblesort(toSort):
    if len(toSort) == 0:
        return toSort
    else:
        n = len(toSort) - 1
        x = 0
        y = 0
        for x in range(len(toSort)):
            while y < n:
                if toSort[y] > toSort[y+1]:
                    tmp = toSort[y]
                    toSort[y] = toSort[y+1]
                    toSort[y+1] = tmp
                y = y + 1
            y = 0
            n = n - 1

        return toSort


# Insertion Sort
# Parameters: An array to sort
# Return: A sorted array
def insertionsort(toSort):
    if len(toSort) == 0: 
        return toSort
    else:
        sorted = [toSort[0]]
        for x in range(1, len(toSort)):
            y = 0
            while y < len(sorted) and sorted[y] < toSort[x]:
                y = y + 1
            sorted.insert(y, toSort[x])
            y = 0
        return sorted


# Merge Sort
# Parameters: An array to sort
# Return: A sorted array        
def mergesort(toSort):
    import math
    if len(toSort) > 1:
        middle = len(toSort) / 2
        floorVal = math.floor(middle)
        list1 = []
        list2 = []
        for x in range(floorVal):
            list1.append(toSort[x])
        for x in range(int(middle), len(toSort)):
            list2.append(toSort[x])
        result1 = mergesort(list1)
        result2 = mergesort(list2)
        res = merge(result1, result2)
        return res
    else:
        return toSort

# Merges two arrays together (Helper function for mergesort)
# Parameters: 2 arrays to be merged
# Result: A single array formed from merging the two arrays 
def merge(toMerge1, toMerge2):
    merged = []
    while len(toMerge1) != 0 and len(toMerge2) != 0:
        if toMerge1[0] <= toMerge2[0]:
            toAppend = toMerge1[0]
            toMerge1.remove(toAppend)
            merged.append(toAppend)
        else:
            toAppend = toMerge2[0]
            toMerge2.remove(toAppend)
            merged.append(toAppend)

    while len(toMerge1) != 0:
        toAppend = toMerge1[0]
        toMerge1.remove(toAppend)
        merged.append(toAppend)

    while len(toMerge2) != 0:
        toAppend = toMerge2[0]
        toMerge2.remove(toAppend)
        merged.append(toAppend)
    return merged

# test casees for each alogrithm

def testBubbleSort(test, correct):
    print("\nTesting Bubble-sort")
    for x in range(len(test)):
        if bubblesort(test[x]) == correct[x]:
            print(str(x+1) + " - Pass")
        else:
            print(str(x+1) + " - Fail")
    print("-----------------------------------------")

def testInsertionSort(test, correct):
    print("\nTesting Insertion-sort")
    for x in range(len(test)):
        if insertionsort(test[x]) == correct[x]:
            print(str(x+1) + " - Pass")
        else:
            print(str(x+1) + " - Fail")
    print("-----------------------------------------")

def testMergeSort(test, correct):
    print("\nTesting Merge-sort:")
    for x in range(len(test)):
        if mergesort(test[x]) == correct[x]:
            print(str(x+1) + " - Pass")
        else:
            print(str(x+1) + " - Fail")
    print("-----------------------------------------")

def main():
    test = [[4,6,10,20,30,40,56,70,100,340],[2,43,1,3,8,56,1,3,0],[34,5,2,242,76,10,11,20],
    [-1,232,-4,5,-555,32,21, 544, -34],[23,44,-1, 34,4, 66, 7, 44, 3], [1,1,1,1,1,1,1,1]]
    correct = [[4,6,10,20,30,40,56,70,100,340], [0,1,1,2,3,3,8,43,56], [2,5,10,11,20,34,76,242],
    [-555,-34,-4,-1,5,21,32,232,544],[-1,3,4,7,23,34,44,44,66],[1,1,1,1,1,1,1,1] ]
    testBubbleSort(test, correct)
    testInsertionSort(test, correct)
    testMergeSort(test, correct)

if __name__ == "__main__":
    main()
