from random import randint


def selection_sort(unsorted_list):
    for i in range(0, len(unsorted_list)-1):
        for j in range(i, len(unsorted_list)):
            a = unsorted_list[i]
            b = unsorted_list[j]
            if unsorted_list[i] > unsorted_list[j]:
                unsorted_list[j] = a
                unsorted_list[i] = b
    return unsorted_list


numbers = []
for integers in range(50):
    numbers.append(randint(1, 100))
selection_sort(numbers)
print(numbers)
