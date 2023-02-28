answer = 0
def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt
    for i in range(len(dungeons)):
        if visited[i] == 0:
            if dungeons[i][0] <= k:
                visited[i] = 1
                dfs(k - dungeons[i][1], cnt+1, dungeons)
                visited[i] = 0
    

def solution(k, dungeons):
    # k = 유저의 현재 피로도
    # [최소 필요 피로도, 소모 피로도]
    global visited
    visited = [0 for _ in range(len(dungeons))]
    dfs(k, 0, dungeons)
    return answer
