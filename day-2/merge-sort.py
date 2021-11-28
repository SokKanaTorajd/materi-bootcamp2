def mergeSort(array):
    if len(array) > 1:
        p = len(array)//2
        left = array[:p]
        right = array[p:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i+=1

            else:
                array[k] = right[j]
                j+=1
            k+=1

            print(array)

        while i < len(left):
            array[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            array[k] = right[j]
            j+=1
            k+=1

    return array

def printArray(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

if __name__=='__main__':
    values = [11, 123, 32, 2, 12, 46, 75]
    print(values)
    sorted = mergeSort(values)
    printArray(sorted)