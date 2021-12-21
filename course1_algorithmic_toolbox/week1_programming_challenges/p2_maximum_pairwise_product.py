# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# Find the maximum product of two distinct numbers in a sequence of non-negative integers.

# O(n^2)
def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


# O(n)
def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    max_index_1 = -1
    for i in range(0, len(numbers)):
        if max_index_1 == -1 or numbers[i] > numbers[max_index_1]:
            max_index_1 = i

    max_index_2 = -1
    for i in range(0, len(numbers)):
        if i != max_index_1 and (max_index_2 == -1 or numbers[i] > numbers[max_index_2]):
            max_index_2 = i

    return numbers[max_index_1] * numbers[max_index_2]


if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
