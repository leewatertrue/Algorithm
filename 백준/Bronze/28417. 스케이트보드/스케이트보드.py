fin=[]
People=int(input())
for i in range(People):
    score=list(map(int, input().split()))
    score[:2]=sorted(score[:2])
    score[2:]=sorted(score[2:])
    fin.append(score[1]+score[5]+score[6])
fin.sort()
print(fin[-1])