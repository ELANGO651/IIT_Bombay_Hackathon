
from collections import deque
# The code starts by importing the deque class from the collections module.
#  deque is used to create a queue data structure, which will be used to store the bowlers.

# The function schedule_bowlers takes three parameters: N (the number of bowlers), Q (the number of balls each bowler throws at a time),
#  and bowlers (a list containing the details of each bowler).

# Inside the function, a deque object named queue is created to store the bowlers' information. 
# finished_bowlers is an empty list that will later store the order in which the bowlers finish their rounds.

# The j variable is initialized to 0, which will be used to assign unique IDs to the bowlers.

# The loop for subls in bowlers iterates through each sublist in the bowlers list.
#  An ID (j) is appended to each sublist, representing the unique identifier for the bowler. This ID will help keep track of the order in which the bowlers finish their rounds.

# The for loop for i in range(N) initializes the queue by appending the bowlers' information to the queue deque.


def schedule_bowlers(N, Q, bowlers):
    queue = deque()  # Queue to store bowlers
    finished_bowlers = []  # List to store finished bowlers' order
    j = 0

    # Append unique IDs to each bowler's sublist
    for subls in bowlers:
        subls.append(j)
        j += 1

    # Initialize the queue with bowlers
    for i in range(N):
        queue.append(bowlers[i])
# """he main part of the code is the while loop, which continues until the queue is empty.
#  It processes the ball throwing sequences for each bowler in the queue.

# Inside the loop, bowler_id is retrieved by calling popleft() on the queue,
#  which removes and returns the first bowler from the queue.

# The code checks if the bowler has any balls left before the rest (bowler_id[0] != 0). 
# If so, one ball is thrown by decrementing bowler_id[0] by 1.

# After throwing the ball, the code checks if the bowler has completed the pre-rest throws (bowler_id[0] == 0) but 
# still has balls left for the rest (bowler_id[1] != 0). If true, the code decrements bowler_id[1] by 1 and appends the bowler back to the queue.

# If the bowler has completed all the throws (bowler_id[0] == 0) 
#  the rest time (bowler_id[1] == 0), the code checks if the bowler has any balls left after the rest (bowler_id[2] != 0).
#  If true, the code decrements bowler_id[2] by 1.

# After decrementing the ball count, the code checks 
# if the bowler has completed all the throws (bowler_id[0] == 0), rest time (bowler_id[1] == 0), 
#  post-rest throws (bowler_id[2] == 0). If true, the bowler's ID (bowler_id[3]) is appended to the finished_bowlers list, indicating the order in which the bowler finishes their round.

# The loop continues until all the bowlers in the queue have finished their rounds.

# Finally, the function returns the finished_bowlers list, which contains the order in which the bowlers"""
    # Process the ball throwing sequences until the queue is empty
    while len(queue) > 0:
        bowler_id = queue.popleft()
        # Determine the maximum number of balls to throw in this turn
        max_throw = min(Q, bowler_id[0])

        # Determine the number of balls to throw after the rest time
        after_max_throw = min(Q, bowler_id[2])

        # Check if the bowler has balls left before the rest time
        if bowler_id[0] != 0:
            bowler_id[0] -= max_throw

            # If the bowler has completed all throws, add their ID to the finished bowlers' list
            if bowler_id[0] == 0 and bowler_id[1] == 0 and bowler_id[2] == 0:
                finished_bowlers.append(bowler_id[3])
            else:
                queue.append(bowler_id)
            
        # Check if the bowler has rest time remaining
        if bowler_id[0] == 0 and bowler_id[1] != 0:
            bowler_id[1] -= 1
            queue.append(bowler_id)

        # Check if the bowler has balls left after the rest time
        elif bowler_id[0] == 0 and bowler_id[1] == 0 and bowler_id[2] != 0:
            bowler_id[2] -= after_max_throw

            # If the bowler has completed all throws, add their ID to the finished bowlers' list
            if bowler_id[0] == 0 and bowler_id[1] == 0 and bowler_id[2] == 0:
                finished_bowlers.append(bowler_id[3])
            else:
                queue.append(bowler_id)

    print(finished_bowlers)
    return finished_bowlers


bowlers = []
input_line = input()
N, Q = map(int, input_line.split())

# Collect input details for each bowler
for l in range(N):
    input_str = input()
    values = list(map(int, input_str.split()))
    bowlers.append(values)

# Call the function and store the result
result = schedule_bowlers(N, Q, bowlers)

# Print the order in which bowlers finished their rounds
print(' '.join(map(str, result)))
