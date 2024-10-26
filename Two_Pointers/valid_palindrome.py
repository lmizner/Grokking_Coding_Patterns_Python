def is_palindrome(s):
  # Initialize pointer 1 at the start of the string and pointer 2 at end of the string
  pointer_1 = 0
  pointer_2 = len(s) - 1
  
  # Continue to loop until the pointers meet at the midpoint
  while pointer_1 <= pointer_2:
    # If there's a match, move pointers inward
    if s[pointer_1] == s[pointer_2]:
      pointer_1 += 1 
      pointer_2 -= 1
    else:
      # If there's no match
      return False
  # If we make it to the midpoint and all match return True
  return True


# Driver code
def main():
    test_cases = ["RACECAR", "ABBA", "TART"]
    i = 1
    for s in test_cases:
        print("Test Case #", i)
        print(is_palindrome(s))
        print("-" * 100, end="\n\n")
        i = i + 1

if __name__ == '__main__':
    main()
