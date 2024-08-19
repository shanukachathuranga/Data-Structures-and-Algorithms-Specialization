from random import randint


def swap(array, val1, val2):
    temp = array[val1]
    array[val1] = array[val2]
    array[val2] = temp


def partition3(array, left, right):
    m1 = left
    m2 = left
    compare_value = array[left]

    for i in range(left + 1, right + 1):
        if array[i] < compare_value:
            m1 += 1
            swap(array, i, m1)
            m2 += 1
            swap(array, m1, m2)
        elif array[i] == compare_value:
            m2 += 1
            swap(array, i, m2)

    swap(array, left, m1)
    return m1, m2


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
