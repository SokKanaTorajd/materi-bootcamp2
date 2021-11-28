def binarySearch(array, key, low, high):
    if low <= high:
        mid = (low+(high-low))//2
        if key==array[mid]:
            return mid
        elif key > array[mid]:
            return binarySearch(array, key, mid+1, high)
        else:
            return binarySearch(array, key, low, mid-1)
    else:
        return False

# array = ['dennis', 'dini', 'nika', 'burhan', 'laela', 'noviana']
# array = sorted(array)
values = [11, 123, 32, 2, 12, 46, 75]
print(values)

# result = binarySearch(array, 'nika', 0, len(array)-1)
result = binarySearch(values, 46, 0, len(values)-1)

print(result)

# result = binarySearch(array, 'david', 0, len(array)-1)
# print(result)
