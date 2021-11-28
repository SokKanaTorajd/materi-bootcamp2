def bubbleSort(array):
    for i in range(len(array)):
        swapped = False
         for j in range(0, len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

                swapped = True
            # print(array)

            print(f"loop ke-{i}\t{array}")
        if not swapped:
            break

    return array

values = [11, 123, 32, 2, 12, 46, 75]
sorted = bubbleSort(values)
print(sorted)

