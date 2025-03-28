find=input()
re=0
N=int(input())
for _ in range(N):
    real = input()
    real2 = real + real
    if find in real2[:len(real)+len(find)-1]:
        re += 1
print(re)