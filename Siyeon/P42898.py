from queue import Queue


def isPuddle(x, y, puddles):
    for puddle in puddles:
        print({"puddle": puddle})
        if puddle[0] == x+1 and puddle[1] == y+1:
            return True
    return False


def findPath(m, n, puddles):
    dp = [[0 for i in range(m)] for j in range(n)]
    dp[0][0] = 1

    que = Queue()

    #오른쪽
    if not isPuddle(1, 0, puddles):
        que.put((1, 0))
    # 아래쪽
    if not isPuddle(0, 1, puddles):
        que.put((0, 1))

    # 2차배열 안쪽이 x, 바깥이 y
    while que.qsize() > 0:
        now = que.get()
        x = now[0]
        y = now[1]

        # 왼쪽 부모
        if x - 1 >= 0:
            dp[y][x] += dp[y][x - 1]
            dp[y][x] %= 1000000007

        # 위쪽 부모
        if y - 1 >= 0:
            dp[y][x] += dp[y - 1][x]
            dp[y][x] %= 1000000007

        if x + 1 < m and (x+1, y) not in que.queue and not isPuddle(x+1, y, puddles):
            que.put((x + 1, y))
        if y + 1 < n and (x, y+1) not in que.queue and not isPuddle(x, y+1, puddles):
            que.put((x, y + 1))

    return dp[n - 1][m - 1]


def solution(m, n, puddles):
    answer = 0
    answer = findPath(m, n, puddles)
    return answer


if __name__ == '__main__':
    puddles = [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]]
    print(puddles)
    output = solution(7, 4, puddles)
    print(output)
