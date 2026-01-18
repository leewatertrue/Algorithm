t=int(input())
for i in range(t):
    w=[]
    w=input().split()
    result=[]
    for j in range(len(w)):
        result.append(w.pop())
    
    print("Case #"+str(i+1)+": "+" ".join(result))