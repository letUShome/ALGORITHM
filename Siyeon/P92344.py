"""
이미 파괴된 건물도 계속해서 내구도가 하락함(음수로 깎아줘야함)
skill: [1-공격/2-회복, r1, c1, r2, c2, 공격/회복 정도]
좌표는 최대 100만, skill은 25만
"""
import sys
input = sys.stdin.readline


def solution(board, skill):
    answer = 0



    return answer


if __name__ == "__main__":
    board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
    skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
    output = solution(board, skill)
    print(output)
