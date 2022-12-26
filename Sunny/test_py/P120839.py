def solution(rsp):
    answer = ''
    
    i = 0;
    
    while i < len(rsp):
        if rsp[i] == '2':
            answer += '0'
        elif rsp[i] == '0':
            answer += '5'
        else:
            answer += '2'
        i += 1
    
    return answer
