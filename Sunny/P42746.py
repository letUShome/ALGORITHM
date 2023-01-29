
def solution(numbers):
    answer = '';
    
    # dfs로 모든 배열의 원소를 탐색하여 알아내기
    # 어차피 가장 큰 숫자를 만들 경우, 모든 숫자를 이어붙여야 함
    
    numbers = list(map(str, numbers));
    numbers.sort(reverse=True);
    print(numbers)
    
    for i in range(len(numbers)-1):   
        if len(numbers[i]) == len(numbers[i+1]):
            answer += numbers[i]
        else:
            if int(numbers[i] + numbers[i+1]) < int(numbers[i+1] + numbers[i]):
                    tmp = numbers[i+1];
                    numbers[i+1] = numbers[i];
                    numbers[i] = tmp
                    answer += tmp;
            else:
                answer += numbers[i]
                    
    answer += numbers[-1];
    
    if int(answer) == 0:
        answer = "0"

    return answer
