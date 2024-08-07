# n = 5
# vecs = [(1,2),(1,1),(-1,-2),(-2,-3),(-1,-1)]
# vecs = sorted(vecs)
# max_sum = 20
# dp = [[0 for _ in range(max_sum*2+1)] for _ in range(n+1)]
# for i in range(n+1):
#     dp[0]

#  Python implementation of the approach
MAX_SUM = 8
ARR_SIZE = 5
 
# To find the number of subsets with sum equal to 0
# Since S can be negative, we will add MAX_SUM
# to it to make it positive
 
 
def SubsetCnt(arr, n):
    dp = [[0 for i in range(MAX_SUM*2+1)] for j in range(n+1)]
 
    # Initializing first column with 1
    for i in range(n+1):
        dp[i][MAX_SUM] = 1

    # Initializing rest of the matrix with 0
    for i in range(1, MAX_SUM*2+1):
        dp[0][i] = 0
    
    for row in dp:
        print(row)
    print()
    
    # Filling up the dp matrix
    for i in range(1, n+1):
        for j in range(-MAX_SUM, MAX_SUM+1):
            val = arr[i-1]
 
            if j-val+MAX_SUM >= 0 and j-val+MAX_SUM <= MAX_SUM*2:
                dp[i][j+MAX_SUM] += dp[i-1][j-val+MAX_SUM]
 
            if j+MAX_SUM >= 0 and j+MAX_SUM <= MAX_SUM*2:
                dp[i][j+MAX_SUM] += dp[i-1][j+MAX_SUM]
 
    # return final answer
    return dp[n][MAX_SUM]
 
 
# Driver code
if __name__ == '__main__':
    arr = [2, 2, 2, -4, -4]
    n = len(arr)
 
    # function call
    print(SubsetCnt(arr, n))