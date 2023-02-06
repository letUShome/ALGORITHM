def solution(answers):
    answer = []
    n1_answer = []
    n2_answer = []
    n3_answer = []
    
    n2_tmp = [2, 1, 2, 3, 2, 4, 2, 5]
    n3_tmp = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    sum_count = {1:0, 2:0, 3:0}
    
    for i in range(len(answers)):
        # 1번: 1 2 3 4 5 -> (i+1) % 5
        if (i+1) % 5 == 0:
            n1_answer.append(5)
        else:
            n1_answer.append((i+1)%5)
            
        # 2번: 짝수 -> (0, 2, 4, 6, 8)2, 홀수 -> (1, 9)1 (3, 11)3 (5, 13)4 (7, 9)5
        n2_answer.append(n2_tmp[i%8])
        
        # 3번
        n3_answer.append(n3_tmp[i%10])
        
        if n1_answer[i] == answers[i]:
            sum_count[1] += 1
        if n2_answer[i] == answers[i]:
            sum_count[2] += 1
        if n3_answer[i] == answers[i]:
            sum_count[3] += 1
    
    sum_count = sorted(sum_count.items(), reverse=True, key = lambda item: item[1])
    
    print(n1_answer)
    print(n2_answer)
    print(n3_answer)
    print(sum_count)
    
    if(sum_count[0][1] == sum_count[2][1]):
        answer.append(1)
        answer.append(2)
        answer.append(3)
    elif(sum_count[0][1] == sum_count[1][1]):
        answer.append(sum_count[0][0])
        answer.append(sum_count[1][0])
        answer.sort()
    else:
        answer.append(sum_count[0][0])
    
    return answer
