# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# The goal in this code problem is to simulate a sequence of merge operations with tables in a database.

class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
    
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, src, dst):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            return False

        if self.ranks[src_parent] > self.ranks[dst_parent]:
            self.parents[dst_parent] = src_parent
            self.row_counts[src_parent] += self.row_counts[dst_parent]
            self.row_counts[dst_parent] = 0
            self.max_row_count = max(self.max_row_count, self.row_counts[src_parent])
        else:
            self.parents[src_parent] = dst_parent
            self.row_counts[dst_parent] += self.row_counts[src_parent]
            self.row_counts[src_parent] = 0
            self.max_row_count = max(self.max_row_count, self.row_counts[dst_parent])
            
            if self.ranks[src_parent] == self.ranks[dst_parent]:
                self.ranks[dst_parent] += 1

        return True

    def get_parent(self, table):
        if self.parents[table] != table:
            self.parents[table] = self.get_parent(self.parents[table])
        return self.parents[table]

if __name__ == "__main__":
    n_tables, m_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(m_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)
