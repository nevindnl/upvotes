import sys
from collections import deque

def read_input():
    stream = sys.stdin
    line = stream.readline().rstrip("\n")
    n, k = map(lambda x: int(x), line.split())
    line = stream.readline().rstrip("\n")
    upvotes = map(lambda x: int(x), line.split())
    return (n, k, upvotes)

def solve(n, k, upvotes):
    window_size = 1
    non_decreasing_subranges = deque([])
    non_increasing_subranges = deque([])
    difference = 0
    for i in xrange(1, n):
        enqueue(non_decreasing_subranges, upvotes[i] >= upvotes[i - 1])
        enqueue(non_increasing_subranges, upvotes[i] <= upvotes[i - 1])
        difference += non_decreasing_subranges[-1] - non_increasing_subranges[-1]
        window_size += 1
        if window_size == k:
            print(difference)
            difference -= non_decreasing_subranges[0] - non_increasing_subranges[0]
            dequeue(non_decreasing_subranges)
            dequeue(non_increasing_subranges)
            window_size -= 1

def dequeue(subranges):
    if subranges[0] > 1:
        subranges[0] -= 1
    else:
        subranges.popleft()

def enqueue(subranges, cmp):
    if cmp:
        if len(subranges) == 0 or subranges[-1] == 0:
            subranges.append(1)
        else:
            subranges[-1] += 1
    else:
        subranges.append(0)

def solution():
    n, k, upvotes = read_input()
    solve(n, k, upvotes)

solution()
