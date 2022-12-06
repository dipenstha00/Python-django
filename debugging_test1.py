values = [1,2,3,4,5]

def solution(numbers):
    total = 0
    for i, n in enumerate(numbers):
        total += n * (i-1)
    return total

solution(values)