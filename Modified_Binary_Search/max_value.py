# Function to calculate the sum
def calculate_sum(index, mid, n):
    
    # Initialize count
    count = 0

    # Calculate the sume on the left side of the index
    if mid > index:
        count += (mid + mid - index) * (index + 1) // 2
    else:
        count += (mid + 1) * mid // 2 + index - mid + 1

    # Calculate the sum on the right side of the index
    if mid >= n - index:
        count += (mid + mid - n + 1 + index) * (n - index) // 2
    else:
        count += (mid + 1) * mid // 2 + n - index - mid

    # Subtract the mid at the index 
    return count - mid



def max_value(n, index, max_sum):

    # Initialize left and right 
    left = 1
    right = max_sum

    # Binary search for the maximum mid at the index
    while left < right:

        # Check if current mid is a valid maximum mid
        mid = (left + right + 1) // 2

        # Move to right half if valid
        if calculate_sum(index, mid, n) <= max_sum:
            left = mid
        
        # Otherwise, move to left half 
        else:
            right = mid - 1

    # Maximum vlaid mid at index
    return left



# Time Complexity = O(log(maxsum))
# Space Complexity = O(1)



##################################################################



# Driver code
def main():
    input_list = [
    (6, 3, 18),
    (4, 2, 6),
    (3, 0, 3),
    (5, 3, 15),
    (7, 4, 20)]

    for i, (n, index, maxSum) in enumerate(input_list):
        result = max_value(n, index, maxSum)
        print(f"{i + 1}.\tInput: n = {n}, index = {index}, maxSum = {maxSum}")
        print(f"\tMaximum mid at index {index}: {result}")
        print('-' * 100)

if __name__ == "__main__":
    main()

