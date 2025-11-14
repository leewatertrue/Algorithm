def solution(n, m, section):
    answer = 0
    covered=0
    for s in section:
        if s>covered:
            answer+=1
            covered=s+m-1
    return answer