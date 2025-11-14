def solution(numbers):
    numbers.sort()
    answer=numbers[-2]*numbers[-1]
    return answer