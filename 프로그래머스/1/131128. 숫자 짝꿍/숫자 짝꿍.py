from collections import Counter
def solution(x, y):
    answer = ''
    xc=Counter(x)
    yc=Counter(y)
    digits=[]
    for i in range(10):
        digit=str(i)
        count=min(xc.get(digit,0), yc.get(digit,0))
        digits.extend([digit]*count)
    if not digits: return "-1"
    if all (d=='0' for d in digits): return "0"
    digits.sort(reverse=True)
    return "".join(digits)