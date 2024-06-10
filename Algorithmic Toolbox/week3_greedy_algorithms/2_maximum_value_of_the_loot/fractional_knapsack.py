from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0
    count = 0
    vlu_per_wgt = []
    for w in weights:
        vlu = values[count]/w
        vlu_per_wgt.append([count,vlu])

    i = 0
    while len(vlu_per_wgt) > i:
        j = i+1
        while j < len(vlu_per_wgt):
            if vlu_per_wgt[j][1] > vlu_per_wgt[i][1]:
                temp = vlu_per_wgt[j]
                vlu_per_wgt[j] = vlu_per_wgt[i]
                vlu_per_wgt[i] = temp

            j += 1

        i += 1

        total_cap = capacity
        k = 0
        while k < len(vlu_per_wgt):
            if weights[vlu_per_wgt[k][0]] < total_cap:
                total_cap -= weights[vlu_per_wgt[k][0]]
                value += vlu_per_wgt[k][1] * weights[vlu_per_wgt[k][0]]
            else:
                value += vlu_per_wgt[k][1] * total_cap
                return value
            k += 1



    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

# from sys import stdin
#
#
# def optimal_value(capacity, weights, values):
#     value = 0.0
#     n = len(values)
#
#     # Calculate value per weight unit and store along with index
#     vlu_per_wgt = [(values[i] / weights[i], weights[i]) for i in range(n)]
#
#     # Sort items by value per weight unit in descending order
#     vlu_per_wgt.sort(reverse=True, key=lambda x: x[0])
#
#     # Add items to the knapsack
#     for vpu, weight in vlu_per_wgt:
#         if capacity == 0:
#             break
#         amount = min(weight, capacity)
#         value += amount * vpu
#         capacity -= amount
#
#     return value
#
#
# if __name__ == "__main__":
#     data = list(map(int, stdin.read().split()))
#     n, capacity = data[0:2]
#     values = data[2:(2 * n + 2):2]
#     weights = data[3:(2 * n + 2):2]
#     opt_value = optimal_value(capacity, weights, values)
#     print("{:.10f}".format(opt_value))
