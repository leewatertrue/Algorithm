def solution(sch, tim, sta):
    answer = 0
    for i in range(len(sch)):
        h, m=sch[i]//100, sch[i]%100
        m+=10
        if m>=60: 
            m-=60 
            h+=1
        deadline=h*100+m
        valid=True
        for day in range(7):
            weekday=(sta+day-1)%7+1
            if weekday<=5:
                if tim[i][day]>deadline: 
                    valid=False 
                    break
        if valid: answer+=1
    return answer