def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step-1

        while j >= 0 and key < array[j]:
            array[j+1]=array[j]
            j-=1
            print(array)
        array[j+1] = key


    return array

values = [11, 123, 32, 2, 12, 46, 75]
print(insertionSort(values))