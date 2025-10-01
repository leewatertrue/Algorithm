case = 1 

while True:
    ans = 0
    arr = input()
    
    if arr[0] == '-':
        break
    
    sta = []
    
    for s in arr:
        if s == '{':
            sta.append(s)
        else:
            if sta and sta[-1] == '{':
                sta.pop()
            else:
                sta.append(s)
    
    open = sta.count('{')
    close = sta.count('}')
    
    ans = (open + 1) // 2 + (close + 1) // 2
    
    print(f"{case}. {ans}")  
    case += 1 