def binary_search(keys, query):
    left, right = 0, len(keys) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if keys[mid] == query:
            # Move to the left to find the first occurrence
            while mid > 0 and keys[mid - 1] == query:
                mid -= 1
            result = mid
            break
        elif keys[mid] < query:
            left = mid + 1
        else:
            right = mid - 1

    return result


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
