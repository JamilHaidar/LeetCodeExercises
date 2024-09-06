# Solve this problem in python:
# Given a matrix of size r,c, find the minimum difference between the largest and smallest entry for any connected set of at least k entries.
# r,c <= 50, k<=100
def find_min_difference(matrix, k):
    # Initialize variables
    r = len(matrix)
    c = len(matrix[0])
    min_diff = float('inf')

    # Helper function to check if a cell is valid
    def is_valid(i, j):
        return 0 <= i < r and 0 <= j < c

    # Helper function to perform DFS on the matrix
    def dfs(i, j, visited, current_set):
        # Mark the cell as visited
        visited[i][j] = True
        current_set.append(matrix[i][j])

        # Check all neighboring cells
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + dx, j + dy
            if is_valid(ni, nj) and not visited[ni][nj] and matrix[ni][nj] != -1:
                dfs(ni, nj, visited, current_set)

    # Iterate through each cell in the matrix
    for i in range(r):
        for j in range(c):
            # Skip if the cell is already visited or marked as -1
            if matrix[i][j] == -1:
                continue

            # Initialize visited matrix and current set
            visited = [[False] * c for _ in range(r)]
            current_set = []

            # Perform DFS on the current cell
            dfs(i, j, visited, current_set)

            # Check if the current set has at least k entries
            if len(current_set) >= k:
                min_diff = min(min_diff, max(current_set) - min(current_set))

    return min_diff

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
k = 4
result = find_min_difference(matrix, k)
print(result)
