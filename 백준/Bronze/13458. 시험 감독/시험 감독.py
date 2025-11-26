n=int(input())
a=list(map(int, input().split()))
b, c = map(int, input().split())
fs, ss=n, 0
for i in range(len(a)):
    ss=a[i]-b
    if ss>0:
        fs+=(ss+c-1)//c
print(fs)