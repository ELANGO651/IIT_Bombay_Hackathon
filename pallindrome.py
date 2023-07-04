def is_palindrome(input_string):
    """
    Determines whether a given number or string is a palindrome.
    
    Args:
        input_string (str): The input number or string.
        
    Returns:
        str: "YES" if the input is a palindrome, "NO" otherwise.
    """
    # Remove spaces, punctuation, and convert to lowercase
    processed_string = ''.join(ch.lower() for ch in input_string if ch.isalnum())
    
    # Check if the processed string is equal to its reverse
    if processed_string == processed_string[::-1]:
        return "YES"
    else:
        return "NO"


# Example usage
input_value = input()
result = is_palindrome(input_value)
print(result)
