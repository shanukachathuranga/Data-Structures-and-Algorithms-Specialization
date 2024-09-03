def majority_element_naive(elements):
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements):
    count = 0
    candidate = None

    for e in elements:
        if count == 0:
            candidate = e
            count = 1
        elif candidate == e:
            count += 1
        else:
            count -= 1

    count = 0
    for e in elements:
        if e == candidate:
            count += 1

    if count > len(elements) // 2:
        return 1
    else:
        return 0

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
