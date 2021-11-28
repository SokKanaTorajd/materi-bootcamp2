def partition(array, low, high):
    pivot = array[high]
    i = low-1

    for j in range(low, high):
        if array[j] <= pivot:
            i+=1
            (array[i], array[j]) = (array[j], array[i])

    (array[i+1], array[high]) = (array[high], array[i+1])
    print(i+1)
    return i+1

def quickSort(array, low, high):
    if low < high:
        part = partition(array, low, high)
        # LEFT SIDE
        quickSort(array, low, part-1)
        # RIGHT SIDE
        quickSort(array, part+1, high)

    return array

values = [11, 123, 32, 2, 12, 46, 75]
print(values)
sorted_values = quickSort(values, 0, len(values)-1)
print(sorted_values)