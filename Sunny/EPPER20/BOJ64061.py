def solution(board, moves):
    # 터트려져 사라진 인형의 개수를 return
    answer = 0
    s = []

    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1] != 0:
                s.append(board[i][move - 1])
                board[i][move - 1] = 0

                if len(s) > 1:
                    if s[-1] == s[-2]:
                        answer += 2
                        s.pop()
                        s.pop()
                break

    return answer
