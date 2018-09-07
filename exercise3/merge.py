def merge(arr1, arr2):
    # base case: if either array is empty, return the other
    if len(arr1) == []:
        return arr2
    if len(arr2) == []:
        return arr1

    # otherwise, add whichever element is lower to the beginning
    # of the new array, and recursively call merge on the remaining
    # elements of the array
    if arr1[0] < arr2[0]:
        return [arr1[0]] + merge(arr1[1:], arr2)
    return [arr2[0]] + merge(arr1, arr2[1:])


# Test cases!
print("Should be []:", merge([], []))
print("Should be [1]:", merge([1], []))
print("Should be [1]:", merge([], [1]))
print("Should be [1, 2]:", merge([2], [1]))
print("Should be [1, 2, 3, 4, 5, 6, 7]:", merge([2,6,7], [1,3,4,5]))

