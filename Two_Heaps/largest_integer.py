import heapq

def largest_integer(num):
  
    # Convert the number into a list of digits
    digits = [int(d) for d in str(num)]

    # Create two max_heaps for odd and even digits
    odd_heap = []
    even_heap = []

    # Fill the heaps
    for d in digits:
        # Even
        if d % 2 == 0:
            heapq.heappush(even_heap, -d)
        # Odd
        else:
            heapq.heappush(odd_heap, -d)

    # Construct result
    result = []

    for d in digits:
        if d % 2 == 0:
            largest_even = -heapq.heappop(even_heap)
            result.append(largest_even) 
        else:
            largest_odd = -heapq.heappop(odd_heap)
            result.append(largest_odd)

    # Join the result list into a single number (integer)
    return int(''.join(map(str, result)))



# Time Complexity = O(nlogn)
# Space Complexity = O(n)



###############################################################



# Driver Code
def main():
    test_cases = [1234, 65875, 4321, 2468, 98123]
    for num in test_cases:
        print("\tInput number:", num)
        print("\n\tOutput number:", largest_integer(num))
        print("-"*100)

if __name__ == "__main__":
    main()


