def is_palindrome(string):
    
    # Initialize one pointer at the start and one at the end
    start = 0
    end = len(string) - 1
    
    while start < end:
        if string[start] == string[end]:
            start += 1
            end -= 1
        else:
            # If there's a mismatch, check two cases:
            # 1. Skip the start character
            # 2. Skip the end character
            skip_start = check_palindrome(string, start + 1, end)
            skip_end = check_palindrome(string, start, end - 1)
            return skip_start or skip_end
    
    return True

def check_palindrome(string, left, right):
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True



# Driver code
def main():
    test_cases = [
        "madame", 
        "dead", 
        "abca", 
        "tebbem", 
        "eeccccbebaeeabebccceea"
    ]
    
    i = 1
    for s in test_cases:
        print("Test Case #", i)
        print(f"Input: '{s}'")
        result = is_palindrome(s)
        print("Is valid palindrome after at most one removal?:", result)
        print("-" * 100, end="\n\n")
        i += 1

if __name__ == '__main__':
    main()