def longest_repeating_character_replacement(s, k):
    # initialize variables
    string_length = len(s)
    length_of_max_substring = 0
    start = 0
    char_freq = {}
    most_freq_char = 0

    # iterate over the input string
    for end in range(string_length):
        # if the new character is not in the hash map, add it, else increment its frequency
        if s[end] not in char_freq:
            char_freq[s[end]] = 1
        else:
            char_freq[s[end]] += 1

        # update the most frequent char
        most_freq_char = max(most_freq_char, char_freq[s[end]])

        # if the number of replacements in the current window have exceeded the limit, slide the window
        if end - start + 1 - most_freq_char > k:
            char_freq[s[start]] -= 1
            start += 1
        
        # if this window is the longest so far, update the length of max substring
        length_of_max_substring = max(end - start + 1, length_of_max_substring)
        
    # return the length of the max substring with same characters after replacement(s)
    return length_of_max_substring

# Driver code
def main():
    input_strings = ["aabccbb", "abbcb", "abccde", "abbcab", "bbbbbbbbb"]
    values_of_k = [2, 1, 1, 2, 4]

    for i in range(len(input_strings)):
        print(i+1, ".\tInput String: ", input_strings[i], sep="")
        print("\tk: ", values_of_k[i], sep="")
        print("\tLength of longest substring with repeating characters: ", longest_repeating_character_replacement(input_strings[i], values_of_k[i]))
        print("-" * 100)

if __name__ == '__main__':
    main()