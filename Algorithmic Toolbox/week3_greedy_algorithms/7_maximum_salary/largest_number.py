from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a:
        return -1
    else:
        return 1

def largest_number(numbers):
    numbers = list(map(str, numbers))
    # Sort numbers using the custom comparator
    numbers.sort(key=cmp_to_key(compare))
    # Concatenate sorted numbers to form the largest number
    return ''.join(numbers)

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(largest_number(input_numbers))
