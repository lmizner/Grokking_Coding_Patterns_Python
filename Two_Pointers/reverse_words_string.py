def reverse_words(sentence):
  # Remove any leading or trailing spaces from the sentence
  sentence = sentence.strip()
  
  # Split the string into words
  words = sentence.split()
  
  # Reverse order of words using two pointers
  start = 0
  end = len(words) - 1
  
  while start < end:
    words[start], words[end] = words[end], words[start]
    start += 1
    end -= 1
  
  # Join words back into sentence
  return ' '.join(words)




# Driver code
def main():
    string_to_reverse = ["Hello World",
                        "a   string   with   multiple   spaces",
                        "Case Sensitive Test Case 1234",
                        "a 1 b 2 c 3 d 4 e 5",
                        "     trailing spaces",
                        "case test interesting an is this"]

    for i in range(len(string_to_reverse)):
        print(i + 1, ".\tOriginal string: '" + "".join(string_to_reverse[i]), "'", sep='')
        result = reverse_words(string_to_reverse[i])

        print("\tReversed string: '" + "".join(result), "'", sep='')
        print("-" * 100)


if __name__ == '__main__':
    main()
