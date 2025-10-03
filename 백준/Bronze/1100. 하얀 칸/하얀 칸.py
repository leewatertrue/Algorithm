board=[]
for _ in range(8): 
    board.append(input())

count=0
for row in range(8):
    for col in range(8):
        if (row+col)%2==0 and board[row][col]=="F":
            count+=1
print(count)