def find_repeated_sequences(dna, k):
    
    string_length = len(dna)

    # If the string length is less than the substring length
    if string_length < k:
        return set()

    # Define mapping for hash function
    mapping = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    base_value = 4
    numbers = []
    for i in range(string_length):
        numbers.append(mapping.get(dna[i]))

    # Initialize hash function variables
    hash_value = 0
    hash_set = set()
    output = set()

    for i in range(string_length - k + 1):
        # Calculate hash value for the first window
        if i == 0:
            for j in range(k):
                hash_value += numbers[j] * (base_value ** (k - j - 1))
        # Calculate hash value for all other sliding windows        
        else: 
            previous_hash_value = hash_value
            hash_value = ((previous_hash_value - numbers[i - 1] * (base_value ** (k - 1))) * base_value) + numbers[i + k - 1]
        
        # If the hash value is already in the set, add 1
        if hash_value in hash_set:
            output.add(dna[i : i + k])
        
        # Otherwise add the hash value to the set
        hash_set.add(hash_value)

    # Return the repeated dna sequences
    return output


def main():
    inputs_string = ["ACGT", "AGACCTAGAC", "AAAAACCCCCAAAAACCCCCC", "GGGGGGGGGGGGGGGGGGGGGGGGG",
                     "TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT", "TTTTTGGGTTTTCCA",
                     "AAAAAACCCCCCCAAAAAAAACCCCCCCTG", "ATATATATATATATAT"]
    inputs_k = [3, 3, 8, 12, 10, 14, 10, 6]

    for i in range(len(inputs_k)):
        print(i+1, ".\tInput Sequence: \'", inputs_string[i], "\'", sep="")
        print("\tk: ", inputs_k[i], sep="")
        print("\tRepeated Subsequence: ",
              find_repeated_sequences(inputs_string[i], inputs_k[i]))
        print("-"*100)


if __name__ == '__main__':
    main()