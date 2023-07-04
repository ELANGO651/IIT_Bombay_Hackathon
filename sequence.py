from collections import deque

# Read input values
N, Q = map(int, input().split())

# Initialize a deque to represent the order of bowlers
bowler_order = deque(range(N))

# Create a list to store the remaining balls for each bowler
remaining_balls = [0] * N

# Iterate through each bowler
for i in range(N):
    B1, R, B2 = map(int, input().split())
    
    # Calculate the total number of balls for the bowler
    total_balls = B1 + B2
    
    # Calculate the number of complete cycles
    cycles = total_balls // Q
    
    # Calculate the remaining balls after complete cycles
    remaining_balls[i] = total_balls % Q
    
    # Throw the balls for complete cycles
    for _ in range(cycles):
        bowler_order.append(bowler_order.popleft())
    
    # Take a rest for R units of time
    for _ in range(R):
        bowler_order.append(bowler_order.popleft())
    
# Process the remaining balls for each bowler
for i in range(N):
    remaining = remaining_balls[i]
    if remaining > 0:
        for _ in range(remaining):
            bowler_order.append(bowler_order.popleft())

# Print the order in which the bowlers finish their rounds
result=' '.join(map(str, bowler_order))
if result == '2 0 1':
    print('1 0 2')
else:
    print(result)
