def majority_element_naive(elements):
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0

def majority_element(elements):
    count = 0
    candidate = 0
    result = 0
    required_count = len(elements)/2
    # using Boyer Moore Voting Algorithm
    for e in elements:
        # print(f"element: {e}")


        if count == 0:
            candidate = e
            count += 1
            # print(f"candidate changed ----> {candidate}\n")
        elif candidate == e:
            count += 1
        else:
            count -= 1
        # print(f"candidate: {candidate} count: {count}\n")

    count = 0
    for e in elements:
        # print(f"chosen candidate: {candidate}  required count: {required_count}")
        if candidate == e:
            count += 1
        # print(f"count of {candidate} in the array: {count}")

    if count >= required_count:
        result = 1

    return result

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
