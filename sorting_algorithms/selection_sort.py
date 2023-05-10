def selectionSort(array):
    size = len(array)
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):

            if array[j] < array[min_index]:
                min_index = j

        (array[ind], array[min_index]) = (array[min_index], array[ind])


if __name__ == '__main__':
    arr = [5, 1, 324, 21, -34]
    selectionSort(arr)
    print(arr)
