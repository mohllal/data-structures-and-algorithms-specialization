# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# The goal in this code problem is to implement the Rabin–Karp’s algorithm for searching the given pattern in the given text.

def print_occurrences(output):
    print(' '.join(map(str, output)))

def poly_hash_func(string, prime, multiplier):
    hash_value = 0
    for i in range(len(string) - 1, -1, -1):
        hash_value = (hash_value * multiplier + ord(string[i])) % prime
    return hash_value

def rabin_karp(pattern, text):
    t = len(text)
    p = len(pattern)
    prime = 1000000007
    multiplier = 236
    result = []
    pattern_hash = poly_hash_func(pattern, prime, multiplier)
    substr_hashes = [poly_hash_func(text[i:i + p], prime, multiplier) for i in range(t - p + 1)]
    for i in range(t - p + 1):
        if pattern_hash == substr_hashes[i]:
            result.append(i)
    return result

if __name__ == '__main__':
    p, s = (input().rstrip(), input().rstrip())
    occurrences = rabin_karp(p, s)
    print_occurrences(occurrences)