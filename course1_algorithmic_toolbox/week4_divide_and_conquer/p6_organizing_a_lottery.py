# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# The goal is to compute, for each point, the number of segments that contain this point.

def count_segments(segments, points):
    return []

if __name__ == '__main__':
    s, p = (map(int, input().split()))
    segments = []
    for i in range(s):
        segments.append(list(map(int, input().split())))
    points = list(map(int, input().split()))

    res = count_segments(segments, points)
    for x in res:
        print(x, end=' ')