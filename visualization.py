import matplotlib.pyplot as plt

merge_sort_filename = 'merge_sort_times.txt'
quick_sort_filename = 'quick_sort_times.txt'
bubble_sort_filename = 'bubble_sort_times.txt'


def get_input_output_values(filename):

    # generate input and output values
    input_values = []
    output_values = []

    with open(filename) as f:
        for line in f:

            line = line.rstrip()
            splitted = line.split(':')

            numberOfElements = int((splitted[0][2: len(splitted[0]) - 1]))
            timeItTakes = float(splitted[1][: len(splitted[1]) - 1])

            input_values.append(numberOfElements)
            output_values.append(timeItTakes)

    return (input_values, output_values)


if __name__ == '__main__':
    input_values, output_values = get_input_output_values(bubble_sort_filename)

    # generate chart

    fig, ax = plt.subplots()
    ax.plot(input_values, output_values, linewidth=3)

    ax.set_title("Bubble sort times", fontsize=24)
    ax.set_xlabel("Number of elements")
    ax.set_ylabel("Numebr of elements in array")

    ax.tick_params(axis='both', labelsize=14)

    ax.axis([2000, 19000, 0, 30])
    plt.show()
