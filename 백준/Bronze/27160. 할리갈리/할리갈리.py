fruit_map={}
n=int(input())
for _ in range(n):
    card=input()
    fruit, count = card.split()
    fruit_map[fruit] = fruit_map.get(fruit, 0) + int(count)

answer=0
for fruit, count in fruit_map.items():
    if count == 5:
        answer=1

if answer==1:
    print("YES")
else: print("NO")