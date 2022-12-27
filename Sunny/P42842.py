# 노란색 격자를 기준으로 생각할 때
# 2개 -> 1 * 2 -> 6 + 4
# 4개 -> 2 * 2 -> 8 + 4
# 4개 -> 1 * 4 -> 2 + 8 + 4
# 1. yellow의 가로 * 세로의 경우의 수를 찾는다(완전탐색)
# 2. 1의 경우의 수에 맞게 필요한 brown의 수를 세고 올바를 경우 return

# 실패1: for문 두개 돌려서 해결하려고 했는데 생각해보니 시간복잡도가 너무 김
# -> yellow의 가로 * 세로 경우의 수를 찾는 방식을 수정해야 할 것 같다
# : 나눗셈을 사용하면 될 것 같다

def solution(brown, yellow):
    answer = []
    y = 0
    
    for x in range(1, yellow * 2):
        
        if (yellow % x) != 0: 
            continue
        else:
            y = yellow / x
        
        if x * y != yellow or x < y:
                continue
        
        elif (x*2) + (y*2) + 4 == brown:
            print(x, y, yellow, brown) # 확인용
            answer.append(x + 2)
            answer.append(y + 2)
            break
        if(len(answer) >= 2): break
        
                
    return answer
