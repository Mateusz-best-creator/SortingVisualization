def quick_sort(array):
    length = len(array)

    if length <= 1:
        return array

    pivot = array.pop()
    leftArray = []
    rightArray = []

    for num in array:
        if num <= pivot:
            leftArray.append(num)
        else:
            rightArray.append(num)

    return quick_sort(leftArray) + [pivot] + quick_sort(rightArray)


if __name__ == '__main__':
    ar = [5, 1, 324, 21, -34]
    result = quick_sort(ar)
    print(result)
