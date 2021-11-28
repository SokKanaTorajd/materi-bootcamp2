def linear_search(array, key):
    for loc in range(len(array)):
        if array[loc] == key:
            return loc

    return False

array = ['dennis', 'dini', 'nika', 'burhan', 'laela', 'noviana']
print(linear_search(array, 'laela'))
print(linear_search(array, 'tama'))
