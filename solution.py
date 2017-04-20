from collections import deque
def solution(filename):
    f = open(filename, 'r')
    text = f.readlines()
    n, k = map(lambda x: int(x), text[0].split())
    prices = map(lambda x: int(x), text[1].split())
    window_size = 1
    subranges = deque([])
    difference = 0
    for i in range(n):
        if i == 0:
            continue
        enqueue(subranges, cmp(prices[i], prices[i - 1]))
        difference += subranges[-1]
        window_size += 1
        if window_size == k:
            print(difference)
            difference -= subranges[0]
            dequeue(subranges)
            window_size -= 1

def dequeue(subranges):
    first = subranges[0]
    if first < -1:
        subranges[0] += 1
    elif first > 1:
        subranges[0] -= 1
    else:
        subranges.popleft()

def enqueue(subranges, cmp):
    if len(subranges) == 0:
        subranges.append(cmp)
        return
    last = subranges[-1]
    if last < 0 and cmp < 0:
        subranges[-1] -= 1
    elif last > 0 and cmp > 0:
        subranges[-1] += 1
    else:
        subranges.append(cmp)

solution('input.txt')
