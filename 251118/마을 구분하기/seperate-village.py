from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def bfs(r, c, visited):
    q = deque([(r, c)])
    visited[r][c] = True
    count = 1
    
    while q:
        x, y = q.popleft()
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny))
                count += 1
    
    return count

visited = [[False] * n for _ in range(n)]
result = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            result.append(bfs(i, j, visited))

result.sort()
print(len(result))
for size in result:
    print(size)