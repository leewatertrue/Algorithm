import sys
input = sys.stdin.readline

n = int(input())

count = 0 

def solve(current_len):
    global count
    
    if current_len == n:
        count += 1
        return

    for num in range(1, 5):
        
        if current_len + num > n:
            continue
        
        solve(current_len + num)

solve(0)

print(count)