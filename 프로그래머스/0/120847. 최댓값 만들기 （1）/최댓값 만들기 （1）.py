def solution(numbers):
    numbers.sort()
    answer = numbers[0]*numbers[1]
    for n in range(len(numbers)-1):
        if answer<numbers[n]*numbers[n+1]: answer=numbers[n]*numbers[n+1]
    return answer