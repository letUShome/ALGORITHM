def solution(n, computers):
    answer = 0
    check = [False for i in range(n)]
    
    for x in range(n):
        if check[x] == False:
            BFS(n, computers, x, check)
            answer += 1
            
    return answer

def BFS(n, computers, x, check):
    check[x] = True
    queue = []
    queue.append(x)
    
    while len(queue) != 0:
        x = queue.pop(0)
        check[x] = True
        for conn in range(n):
            if conn != x and computers[x][conn] == 1:
                if check[conn] == False:
                    queue.append(conn)
