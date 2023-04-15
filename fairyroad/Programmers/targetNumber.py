from collections import deque

def solution(numbers, target):
    queue = deque()
    result = 0
    queue.append((numbers[0], 0))
    queue.append((numbers[0] * -1, 0))
    while queue:
        x, y = queue.popleft()
        y = y + 1
        if y < len(numbers):
            queue.append((x + numbers[y], y))
            queue.append((x - numbers[y], y))
        else:
            if target == x:
                result += 1
    return result
