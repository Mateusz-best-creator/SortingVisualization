def merge_sort(array):

    if len(array) > 1:
        leftArray = array[:len(array) // 2]
        rightArray = array[len(array) // 2:]

        merge_sort(leftArray)
        merge_sort(rightArray)

        i = 0  # left array index
        j = 0  # right array index
        k = 0  # return array index

        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] < rightArray[j]:
                array[k] = leftArray[i]
                i += 1
            else:
                array[k] = rightArray[j]
                j += 1

            k += 1

        while i < len(leftArray):
            array[k] = leftArray[i]
            i += 1
            k += 1

        while j < len(rightArray):
            array[k] = rightArray[j]
            j += 1
            k += 1


if __name__ == '__main__':
    ar = [5, 1, 324, 21, -34]
    merge_sort(ar)
    print(ar)
