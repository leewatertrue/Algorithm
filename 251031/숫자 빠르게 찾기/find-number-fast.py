import bisect
n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

for i in range(m):
    index=bisect.bisect_left(arr, queries[i])
    if index<len(arr) and arr[index]==queries[i]:
        print(index+1)
    else: print("-1")
    
