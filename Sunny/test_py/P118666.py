def solution(survey, choices):
    answer = ''
    
    tendency = {'R':0, 'T':0, 'C':0, 'F':0,
                'J':0, 'M':0, 'A':0, 'N':0}
    
    for i in range(len(survey)):
        if choices[i] == 4:
            continue
        elif choices[i] == 1 or choices[i] == 2 or choices == 3:
            tendency[survey[i][0]] += (4 - choices[i])
        else:
            tendency[survey[i][1]] += (choices[i] - 4)
    
    if(tendency['R'] >= tendency['T']): answer += 'R'
    else: answer += 'T'
    if(tendency['C'] >= tendency['F']): answer += 'C'
    else: answer += 'F'
    if(tendency['J'] >= tendency['M']): answer += 'J'
    else: answer += 'M'
    if(tendency['A'] >= tendency['N']): answer += 'A'
    else: answer += 'N'
            

    return answer
