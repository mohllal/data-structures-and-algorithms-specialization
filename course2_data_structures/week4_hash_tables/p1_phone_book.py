# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# The goal in this code problem is to implement a simple phone book manager.

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    contacts = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            contacts[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
           if contacts.__contains__(cur_query.number):
            del contacts[cur_query.number]
        else:
            response = 'not found'
            if contacts.__contains__(cur_query.number):
                response = contacts[cur_query.number]
            result.append(response)
    return result

if __name__ == '__main__':
    n = int(input())
    queries = [Query(input().split()) for i in range(n)]
    responses = process_queries(queries)
    write_responses(responses)

