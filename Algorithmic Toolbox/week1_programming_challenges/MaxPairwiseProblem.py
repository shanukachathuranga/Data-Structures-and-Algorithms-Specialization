import random

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
            numbers[first] * numbers[second])
    return max_product


def max_pairwise_product_fast(numbers):
    n = len(numbers)
    max_product = 0
    max_val1 = float('-inf')
    max_val2 = float('-inf')
    max_val1_index = None
    for i in range(n):
        if numbers[i] > max_val1:
            max_val1 = numbers[i]
            max_val1_index = i
    for i in range(n):
        if numbers[i] > max_val2 and i != max_val1_index:
            max_val2 = numbers[i]
            
    return max_val2*max_val1

# if __name__ == '__main__':
#     _ = int(input())
#     input_numbers = list(map(int, input().split()))
#     print(max_pairwise_product_fast(input_numbers))
    
def main():
    while True:
        num_list = [random.randint(1,10000) for _ in range(100)]
        print(num_list)
        test1 = max_pairwise_product(num_list)
        test2 = max_pairwise_product_fast(num_list)
        if test1 == test2:
            print(f"Test1 ({test1}) = Test2 ({test2}) ---> Okay")
        else:
            print(f"Test1 ({test1}) != Test2 ({test2}) ---> ERROR")
            break
    
main()
    
