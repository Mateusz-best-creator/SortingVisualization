from random_array import get_array_of_given_size
from time import time
# sorting algorithms
from sorting_algorithms import quick_sort, merge_sort, bubble_sort, selection_sort

# We will have 10 array, and test how much time take each sorting algorithm
# to sort these array

array = {}

for size in range(2500, 20_000, 2500):
    array[f"{str(size)}"] = get_array_of_given_size(size)


def time_of_particular_sorting(func, array):
    timeStart = time()
    func(array)
    timeEnd = time()

    return float(timeEnd - timeStart)


def get_times_of_sorting(typeOfSortingAlgorithm, nameOfSorting):
    print("jestem")
    results_of_sorting = []
    for key, value in array.items():
        result = {}

        # helper
        print("Time", time_of_particular_sorting(
            typeOfSortingAlgorithm, value))

        result[str(key)] = time_of_particular_sorting(
            typeOfSortingAlgorithm, value)

        results_of_sorting.append(result)

    with open(f"{nameOfSorting}.txt", 'w') as f:
        for data in results_of_sorting:
            f.write(str(data))
            f.write('\n')


if __name__ == '__main__':
    # get_times_of_sorting(quick_sort.quick_sort, 'quick_sort_times')
    # get_times_of_sorting(merge_sort.merge_sort, 'merge_sort_times')
    # get_times_of_sorting(selection_sort.selectionSort, 'selection_sort_times')
    get_times_of_sorting(bubble_sort.bubble_sort, 'bubble_sort_times')
