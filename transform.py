def transform_string(S: str, L: int) -> str:
   
    # Transforms the input string 'S' according to the transformation rules 'L' times.

    # Args:
    #     S (str): The input string containing characters 'x', 'y', and 'z'.
    #     L (int): The number of iterations for the transformation.

    # Returns:
    #     str: The transformed string after 'L' iterations.
   
    for _ in range(L):
        transformed_string = ""
        for char in S:
            if char == 'x':
                transformed_string += 'xyz'
            elif char == 'y':
                transformed_string += 'yxz'
            elif char == 'z':
                transformed_string += 'zxy'
        S = transformed_string
    return S


def find_nth_character(S: str, L: int, N: int) -> str:
 
    # Finds the Nth character in the final transformed string after 'L' iterations.

    # Args:
    #     S (str): The input string containing characters 'x', 'y', and 'z'.
    #     L (int): The number of iterations for the transformation.
    #     N (int): The target character position to find.

    # Returns:
    #     str: The Nth character in the final transformed string.
  
    final_string = transform_string(S, L)
    return final_string[N]  # No need to adjust index, as input is 0-based


# Get input from the user in one line and store it as a tuple
sample_inputs = tuple(input().split())
S, L, N=sample_inputs[0],sample_inputs[1],sample_inputs[2]
# Process each sample input and print the result

result = find_nth_character(S, int(L), int(N))
print(result)
