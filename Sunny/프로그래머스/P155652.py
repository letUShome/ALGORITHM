def solution(s, skip, index):
    answer = ''
    
    skip = list(skip); 
    for i in range(len(skip)):
        skip[i] = ord(skip[i]);
    s = list(s)
    
    for alp in s:
        alp = ord(alp)
        
        cnt = 0;
        while cnt < index:
            if alp + 1 in skip or alp - 25 in skip:
                alp += 1;
            else:
                cnt += 1;
                alp += 1;
            if alp > 122:
                alp -= 26;
            
        answer += chr(alp);

        
    return answer
