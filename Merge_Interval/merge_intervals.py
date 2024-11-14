def merge_intervals(intervals):

    # If intervals is an empty list return None
    if not intervals:
        return None
    
    # Set up an empty list to store merge interval values
    result = []
    # Add the first interval from list of intervals to the list
    result.append([intervals[0][0], intervals[0][1]])

    for i in range(1, len(intervals)):
        # The most recently added interval to the results list
        last_added_interval = result[len(result) - 1]
        
        # Pull the current interval start and end values
        curr_start = intervals[i][0]
        curr_end = intervals[i][1]

        # Pull the previous interval end value
        prev_end = last_added_interval[1]

        # Compare current start with preivous end
        if curr_start <= prev_end:
            # Replace the end interval of the last entry in result with the max
            result[-1][1] = max(curr_end, prev_end)
        else:
            # Add the current interval to the results list
            result.append([curr_start, curr_end])

    return result




# Driver code
def main():
    
    all_intervals = [
    [[1, 5], [3, 7], [4, 6]],
    [[1, 5], [4, 6], [6, 8], [11, 15]],
    [[3, 7], [6, 8], [10, 12], [11, 15]],
    [[1, 5]],
    [[1, 9], [3, 8], [4, 4]],
    [[1, 2], [3, 4], [8, 8]],
    [[1, 5], [1, 3]],
    [[1, 5], [6, 9]],
    [[0, 0], [1, 18], [1, 3]]
    ]

    for i in range(len(all_intervals)):
        print(i + 1, ". Intervals to merge: ", all_intervals[i], sep="")
        result = merge_intervals(all_intervals[i])
        print("   Merged intervals:\t", result)
        print("-"*100)

if __name__ == '__main__':
    main()