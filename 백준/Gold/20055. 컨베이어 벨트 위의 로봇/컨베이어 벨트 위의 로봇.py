n, k=map(int, input().split())
a=list(map(int, input().split()))
robot=[False]*n
step=0

while True:
    step+=1
    a=[a[-1]]+a[:-1]
    robot=[robot[-1]]+robot[:-1]
    robot[n-1]=False
    for i in range(n-2, -1, -1):
        if robot[i+1]==False and robot[i]==True and a[i+1]>=1: 
            a[i+1]-=1
            robot[i+1]=True
            robot[i]=False
    robot[n-1] = False
    if a[0]>=1 and robot[0]==False: 
        a[0]-=1
        robot[0]=True
    if a.count(0)>=k: break

print(step)