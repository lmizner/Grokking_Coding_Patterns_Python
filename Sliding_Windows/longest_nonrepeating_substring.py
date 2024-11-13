def find_longest_substring(input_str):
    # Check the length of input_str
    if len(input_str) == 0:
        return 0

    window_start, longest, window_length = 0, 0, 0

    last_seen_at = {}

    # Traverse str to find the longest substring 
    # without repeating characters.
    for index, val in enumerate(input_str):
        # If the current element is not present in the hash map,
        # then store it in the hash map with the current index as the value.
        if val not in last_seen_at:
            last_seen_at[val] = index
        else:
            # If the current element is present in the hash map,
            # it means that this element may have appeared before.
            # Check if the current element occurs before or after `window_start`.
            if last_seen_at[val] >= window_start:
                window_length = index - window_start
                if longest < window_length:
                    longest = window_length
                window_start = last_seen_at[val] + 1

            # Update the last occurrence of
            # the element in the hash map
            last_seen_at[val] = index

    index += 1
    # Update the longest substring's
    # length and starting index.
    if longest < index - window_start:
        longest = index - window_start

    return longest


# Driver code
def main():
    string = [
        "abcabcbb",
        "pwwkew",
        "bbbbb",
        "ababababa",
        "",
        "ABCDEFGHI",
        "ABCDEDCBA",
        "AAAABBBBCCCCDDDD",
    ]
    for i in range(len(string)):
        print(i + 1, ". \t Input String: ", string[i], sep="")
        print("\t Length of longest substring: ",
                (find_longest_substring(string[i])))
        print("-" * 100)


if __name__ == "__main__":
    main()