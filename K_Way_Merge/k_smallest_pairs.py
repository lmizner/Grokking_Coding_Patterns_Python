from heapq import *


def k_smallest_pairs(list1, list2, k):

    # Initialize a min-heap
    min_heap = []

    # Store results
    pairs = []

    # Iterate over length of list1
    for i in range(min(k, len(list1))):
        
        # Compute sum of pairs and place in min_heap
        heappush(min_heap, (list1[i] + list2[0], i, 0))

    counter = 1

    # Iterate over elements in min_heap up to k
    while min_heap and counter <= k:

        # Pull sum of pairs, i and j from top element of min_heap
        sum_of_pairs, i, j = heappop(min_heap)

        # Add pairs with smallest sum to results list
        pairs.append([list1[i], list2[j]])

        # Increment index
        next_element = j + 1

        # If next element is available, add it to the heap
        if len(list2) > next_element:
            heappush(min_heap, (list1[i] + list2[next_element], i, next_element))

        counter += 1

    # Return pairs with smallest sums
    return pairs



# Time Complexity = O(klogm)
# Space Complexity = O(m)



####################################################################



# Driver code
def main():
    list1 = [[2, 8, 9],
             [1, 2, 300],
             [1, 1, 2],
             [4, 6],
             [4, 7, 9],
             [1, 1, 2]]

    list2 = [[1, 3, 6],
             [1, 11, 20, 35, 300],
             [1, 2, 3],
             [2, 3],
             [4, 7, 9],
             [1]]

    k = [9, 30, 1, 2, 5, 4]

    for i in range(len(k)):
        print(i + 1, ".\t Input pairs: ", list1[i], ", ", list2[i],
              f"\n\t k = {k[i]}", sep="")
        print("\t Pairs with the smallest sum are: ",
              k_smallest_pairs(list1[i], list2[i], k[i]), sep="")
        print("-" * 100)

if __name__ == '__main__':
    main()
