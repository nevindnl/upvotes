from collections import deque
def solution(filename):
    f = open(filename, 'r')
    text = f.readlines()
    n, k = map(lambda x: int(x), text[0].split())
    upvotes = map(lambda x: int(x), text[1].split())
    window_size = 1
    non_decreasing_subranges = deque([])
    non_increasing_subranges = deque([])
    difference = 0
    for i in range(n):
        if i == 0:
            continue
        enqueue(non_decreasing_subranges, upvotes[i] >= upvotes[i - 1])
        enqueue(non_increasing_subranges, upvotes[i] <= upvotes[i - 1])
        difference += non_decreasing_subranges[-1] - non_increasing_subranges[-1]
        print(non_decreasing_subranges, non_increasing_subranges, difference)
        window_size += 1
        if window_size == k:
            print(difference)
            difference -= non_decreasing_subranges[-1] - non_increasing_subranges[-1]
            dequeue(non_decreasing_subranges)
            dequeue(non_increasing_subranges)
            print(non_decreasing_subranges, non_increasing_subranges, difference)
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

solution('input.txt')
