def calculate(brown, x, y):
    if x * 2 + y * 2 + 4 == brown:
        return True
    else:
        return False


def solution(brown, yellow):
    answer = []
    max = yellow + 1
    if yellow > 1:
        max = yellow // 2 + 1

    for i in range(1, max):
        x = yellow // i
        y = i

        #i는 생각하지않고 그냥 1부터 max까지 +1씩하는거니까
        #그중에서 1)yellow의 약수에 해당하는지, 2)그리고 곱의쌍은 어차피 yellow의 반까지만 생각하면되니까 x>=y일때까지만
        if yellow % i == 0 and x >= y:
            result = calculate(brown, x, y)
            if result == True:
                answer = [x + 2, y + 2]
    return answer