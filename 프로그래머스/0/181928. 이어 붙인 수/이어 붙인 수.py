def solution(num):
    p=[]
    m=[]
    for i in range(len(num)):
        if num[i]%2==0: p.append(str(num[i]))
        else: m.append(str(num[i]))
    A="".join(p)
    B="".join(m)
    answer = int(A)+int(B)
    return answer