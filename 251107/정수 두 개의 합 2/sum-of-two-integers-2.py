import sys
input = sys.stdin.readline

N, k = map(int, input().split())
arr = [int(input()) for _ in range(N)]

arr.sort()

left = 0
right = N - 1
count = 0

while left < right:
    current_sum = arr[left] + arr[right]

    if current_sum <= k:
        count += (right - left)
        left += 1
        
    else: 
        right -= 1
        
print(count)