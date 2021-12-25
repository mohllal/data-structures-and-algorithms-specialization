# python3 (this comment tells the grading system at Coursera to use python3 rather than python2)

# Given 𝑛 points on a plane, find the smallest distance between a pair of two (different) points. 
# Recall that the distance between points (𝑥1, 𝑦1) and (𝑥2, 𝑦2) is equal to √︀(𝑥1 − 𝑥2)^2 + (𝑦1 − 𝑦2)^2.

def minimum_distance(points):
    return 0

if __name__ == '__main__':
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))

    print(minimum_distance(points))