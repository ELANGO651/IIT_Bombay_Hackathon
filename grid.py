def minimum_cost(n, grid):
    
    # Calculates the minimum cost to pass through the grid.

    # Args:
    #     n (int): The size of the grid.
    #     grid (List[List[int]]): The 2D grid containing the cost values.

    # Returns:
    #     int: The minimum cost to pass through the grid.

    # Explanation:
    # - Creates a 2D matrix 'dp' to store the minimum cost at each cell.
    # - Initializes the first cell with its own cost.
    # - Fills the first row and first column with cumulative costs.
    # - Calculates the minimum cost for each remaining cell based on adjacent cells.
    # - Returns the minimum cost at the bottom right cell.

    # Time Complexity:
    # - The algorithm iterates over each cell in the grid once, resulting in O(n^2) complexity.

    # Space Complexity:
    # - The space used by the 'dp' matrix is proportional to the size of the grid, resulting in O(n^2) complexity.
    

    # Create a 2D matrix to store the minimum cost at each cell
    dp = [[0] * n for _ in range(n)]

    # Initialize the first cell with its own cost
    dp[0][0] = grid[0][0]

    # Fill the first row
    for i in range(1, n):
        dp[0][i] = dp[0][i - 1] + grid[0][i]

    # Fill the first column
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # Calculate the minimum cost for each cell
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

    # Return the minimum cost at the bottom right cell
    return dp[n - 1][n - 1]


# Read the input size
n = int(input())

# Read the grid values
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row) #Add the row value at the last

# Calculate and print the minimum cost
result = minimum_cost(n, grid)
print(result)
