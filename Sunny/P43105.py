def solution(triangle):
    answer = 0
    
    dp = [[0 for j in range(len(triangle))] for i in range(len(triangle))]
    
    dp[0][0] = triangle[0][0]
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j]+ triangle[i][j], dp[i-1][j-1]+ triangle[i][j]) 
        
    # print(dp)
    
    answer = max(dp[len(triangle) -1])
    
    return answer
