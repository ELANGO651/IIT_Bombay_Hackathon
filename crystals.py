#The function maximize_crystal_glow takes the size of the crystal array n, the number of days k, 
#The number of consecutive crystals exposed to sunlight each day w, and the array representing the glow of the crystals A

def maximize_crystal_glow(n, k, w, A):
    # Split the crystal array into the first two windows (The code splits the crystal array into two windows, list1 and list2, each of size w)
    list1 = A[:w]  # First window of crystals
    list2 = A[w:2 * w]  # Second window of crystals

    min_glow = min(max(list1), max(list2))  # Initial minimum glow is the lowest maximum in the two windows
#The code then iterates k times to update the minimum glow and 
# increment the glow of the crystals in the window with the higher maximum.
    for _ in range(k):
        # Determine the maximum glow in the current window
        max_glow = max(list1) if min_glow == max(list2) else max(list2)

        # Update the minimum glow
        min_glow = min(min_glow, max_glow)

        # Increment the glow of the crystals in the window with the higher maximum
        if max_glow == max(list1):
            list2 = [crystal + 1 for crystal in list2]
        else:
            list1 = [crystal + 1 for crystal in list1]

    # Combine the two windows
    combined_list = list1 + list2

    # Return the minimum glow from the combined list
    return min(combined_list)


# Read input values
n = int(input())
k = int(input())
w = int(input())
A = list(map(int, input().split()))

# Call the function and print the result
result = maximize_crystal_glow(n, k, w, A)
print(result)
