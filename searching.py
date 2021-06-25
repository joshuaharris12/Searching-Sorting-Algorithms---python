# Linear Search
# Parameters: 1. A sorted array  2. A search value
# Returns: The index of the search value or -1 if not found
def linearSearch(toSearch, toFind):
    if len(toSearch) == 0:
        return -1
    else:
        for i in range(0, len(toSearch)):
            if toSearch[i] == toFind:
                return i
            else:
                continue
        return -1


# Binary Search
# Parameters: 1. A sorted array  2. A search value
# Returns: The index of the search value or -1 if not found
def binarysearch(toSearch, toFind):
    if len(toSearch) == 0:
        return -1
    else:
        left = 0
        right = len(toSearch) - 1

        while (left <= right):
            middle = int((left + right) / 2)
            if toSearch[middle] == toFind:
                return middle
            else:
                if toSearch[middle] < toFind:
                    left = middle + 1
                else:
                    right = middle - 1
        
        return -1

def main():
    import numpy as np

    toFind = 30
    arr = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    binaryindex = binarysearch(arr, toFind)
    print(binaryindex)
    linearindex = linearSearch(arr, toFind)
    print(linearindex)




if __name__ == "__main__":
    main()