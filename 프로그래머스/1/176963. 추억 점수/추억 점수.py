def solution(name, yearn, photo):
    answer = []
    peo=len(name)
    for i in range(len(photo)):
        score=0
        for j in photo[i]:
            for n in range(len(name)):
                if j==name[n]: score+=yearn[n]
        answer.append(score)
    return answer