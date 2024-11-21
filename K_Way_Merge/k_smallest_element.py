from heapq import *

def kth_smallest_element(matrix, k):

    # Store number of rows in matrix
    row_count = len(matrix)

    # Initialize min_heap to track smallest elements
    min_numbers = []

    for i in range(min(row_count, k)):

        # Push the first element of each row in min_heap
        heappush(min_numbers, (matrix[i][0], i, 0))

    numbers_checked = 0
    smallest_element = 0

    # Iterate over elements in min_heap
    while min_numbers:

        # Pull smallest number form top of heap
        smallest_element, row_index, col_index = heappop(min_numbers)
        numbers_checked += 1

        # When numbers_checked = k, return smallest element
        if numbers_checked == k:
            break

        # If curren popped element has a next, add it to the min_heap
        if col_index + 1 < len(matrix[row_index]):
            heappush(min_numbers, (matrix[row_index][col_index + 1], row_index, col_index + 1))

    #return k smallest element
    return smallest_element



# Time Complexity = O(klog(min(n, k)))
# Space Complexity = O(n)



####################################################################



# Driver code
def main():

    # multiple inputs for efficient results
    matirx = [
        [[2, 6, 8],
         [3, 7, 10],
         [5, 8, 11]],

        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]],

        [[5]],

        [[2, 5, 7, 9, 10],
        [4, 6, 8, 12, 14],
        [11, 13, 16, 18, 20],
        [15, 17, 21, 24, 26],
        [19, 22, 23, 25, 28]],

        [[3, 5, 7, 9, 11, 13],
        [6, 8, 10, 12, 14, 16],
        [15, 17, 19, 21, 23, 25],
        [18, 20, 22, 24, 26, 28],
        [27, 29, 31, 33, 35, 37],
        [30, 32, 34, 36, 38, 40]]
    ]

    k = [3, 4, 1, 10, 15]

    # loop to execute till the length of list k
    for index in range(len(k)):
        print(index + 1, ".\t Input matrix: ",
              matirx[index], f"\n\t k = {k[index]}", sep="")
        print("\t Kth smallest number in the matrix is: ",
              kth_smallest_element(matirx[index], k[index]), sep="")
        print("-" * 100)

if __name__ == '__main__':
    main()


