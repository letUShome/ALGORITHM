def solution(array, commands):
    answer = []
    
    for cmd in commands:
        tmp_list = array[cmd[0]-1:cmd[1]]
        tmp_list.sort()
        print(tmp_list)
        answer.append(tmp_list[cmd[2]-1])
    
    return answer
