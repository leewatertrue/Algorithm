n=int(input())
num=list(map(int, input().split()))
m=list(map(int, input().split()))
ans=[]
def back(i, val):
    if i==n:
        ans.append(val)
        return
    if m[0]>0:
        m[0]-=1
        back(i+1, val+num[i])
        m[0]+=1
    if m[1]>0:
        m[1]-=1
        back(i+1, val-num[i])
        m[1]+=1
    if m[2]>0:
        m[2]-=1
        back(i+1, val*num[i])
        m[2]+=1
    if m[3]>0:
        m[3]-=1
        back(i+1, int(val/num[i]))
        m[3]+=1

back(1, num[0])
print(max(ans))
print(min(ans))