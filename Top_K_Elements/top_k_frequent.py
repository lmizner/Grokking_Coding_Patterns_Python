from heapq import heappush, heappop

def top_k_frequent(arr, k):

    # Dictionary to save the frequency of each number
    num_frequency_map = {}
    
    # Loop through array, adding all elements to dictionary
    for num in arr:
        num_frequency_map[num] = num_frequency_map.get(num, 0) + 1
    
    # Initialize min heap
    top_k_elements = []

    for num, frequency in num_frequency_map.items():
        heappush(top_k_elements, (frequency, num))

        if len(top_k_elements) > k:
            heappop(top_k_elements)

    # Create list of top k numbers
    top_numbers = []
    
    while top_k_elements:
        top_numbers.append(heappop(top_k_elements)[1])

    return top_numbers



# Time Complexity = O(nlogn)
# Space Complexity = O(n+k)



############################################################################



# Driver code
def main():
    arr = [[1, 3, 5, 12, 11, 12, 11, 12, 5], [1, 3, 5, 14, 18, 14, 5],
           [2, 3, 4, 5, 6, 7, 7], [9, 8, 7, 6, 6, 5, 4, 3, 2, 1], 
           [2, 4, 3, 2, 3, 4, 5, 4, 4, 4], [1, 1, 1, 1, 1, 1], [2, 3]]
    k = [3, 2, 1, 1, 3, 1, 2]

    for i in range(len(k)):
        print(i+1, ". \t Input: (", arr[i], ", ", k[i], ")", sep="")
        print("\t Top", k[i], "frequent Elements: ",
              top_k_frequent(arr[i], k[i]))
        print("-"*100)

if __name__ == '__main__':
    main()



