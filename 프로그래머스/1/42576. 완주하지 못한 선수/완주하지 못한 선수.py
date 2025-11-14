from collections import Counter
def solution(participant, completion):
    pc = Counter(participant)
    cc = Counter(completion)
    
    for name in pc:
        if pc[name] != cc[name]:
            return name