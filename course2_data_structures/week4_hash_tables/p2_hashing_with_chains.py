# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# The goal in this code problem is to implement a hash table with lists chaining.

from collections import deque

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.index = int(query[1])
        else:
            self.word = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.hash_table = list(deque() for _ in range(self.bucket_count))

    def hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        if len(chain) > 0:
            print(' '.join(chain))
        else: print()

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            self.write_chain(self.hash_table[query.index])
        else:
            hash = self.hash_func(query.word)
            if query.type == "add":
                if query.word not in self.hash_table[hash]:
                    self.hash_table[hash].appendleft(query.word)
            elif query.type == "del":
                if query.word in self.hash_table[hash]:
                    self.hash_table[hash].remove(query.word)
            elif query.type == "find":
                self.write_search_result(query.word in self.hash_table[hash])

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
