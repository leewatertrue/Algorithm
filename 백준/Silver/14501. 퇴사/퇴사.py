n=int(input())
d=[]
w=[]
for i in range(n):
    a, b=map(int, input().split())
    d.append(a)
    w.append(b)

def ans(day, money):
    if day >=n: return money
    answer=ans(day+1, money)

    if day+d[day]<=n:
        answer=max(answer, ans(day+d[day], money+w[day]))
    
    return answer

print(ans(0,0))