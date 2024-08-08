from sys import stdin


# weights = [20, 10, 40, 30, 50]
# values = [100, 60, 140, 120, 160]
# # [5,6,3.5,4,3.2]

def maximum_value_sort(weights,values):
    value_per_weight_list = []
    for i in range(len(weights)):
        value_per_weight_list.append([values[i]/weights[i],i])

    value_per_weight_list = sorted(value_per_weight_list,reverse=True)
    return value_per_weight_list



def optimal_value(capacity, weights, values):
    sorted_value_per_weight_list = maximum_value_sort(weights,values)
    i = 0
    value = 0
    while i < len(weights):

        if capacity <=0:
            return value

        max_value = sorted_value_per_weight_list[i][0]
        a = min(capacity,weights[sorted_value_per_weight_list[i][1]])
        value += a * max_value
        capacity -= a
        i+=1

    return value

# print(optimal_value(50,weights,values))


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
