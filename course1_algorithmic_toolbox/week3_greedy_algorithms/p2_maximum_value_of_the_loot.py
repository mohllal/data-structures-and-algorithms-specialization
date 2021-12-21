# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# Implement an algorithm for the fractional knapsack problem.

# O(n log n)
def get_sorted_value_per_weight(weights, values):
    sorted_value_per_weight = []
    for i in range(len(weights)):
        sorted_value_per_weight.append((values[i] / weights[i], weights[i]))
    sorted_value_per_weight.sort(reverse=True, key=lambda x: x[0])
    return sorted_value_per_weight

# O(n)
def get_optimal_value(capacity, weights, values):
    sorted_value_per_weight = get_sorted_value_per_weight(weights, values)
    value = 0.
    
    for i in range(len(sorted_value_per_weight)):
        if capacity == 0:
            return value
        if sorted_value_per_weight[i][1] >= capacity:
            value += capacity * sorted_value_per_weight[i][0]
            capacity = 0
        else:
            value += sorted_value_per_weight[i][0] * sorted_value_per_weight[i][1]
            capacity -= sorted_value_per_weight[i][1]

    return value


if __name__ == "__main__":
    n, capacity = map(int, input().split())
    values, weights  = [], []
    for i in range(n):
        c = input()
        v, w = map(int, c.split())
        values.append(v)
        weights.append(w)
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))