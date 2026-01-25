from collections import Counter
def solution(x,y):
    ans=[]
    xc=Counter(x)
    yc=Counter(y)
    for i in range(10):
        digit=str(i)
        count=min(xc.get(digit,0), yc.get(digit, 0))
        ans.extend(digit*count)
    if not ans: return "-1"
    if all (d=='0' for d in ans): return "0"
    ans.sort(reverse=True)
    return "".join(ans)