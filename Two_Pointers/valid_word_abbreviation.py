def valid_word_abbreviation(word, abbr):

  # Initialize pointer start locations
  word_pointer = 0
  abbr_pointer = 0
  
  # Continue loop until end of abbr in reached
  while abbr_pointer < len(abbr):
    
    # Check if alphabetical character
    if abbr[abbr_pointer].isalpha():
     
      # Verify that alphabetical characters match between word and abbr
      if word_pointer < len(word) and word[word_pointer] == abbr[abbr_pointer]:  
        word_pointer += 1
      
      else:
        return False
        
      abbr_pointer += 1
    
    # Check if numerical character
    elif abbr[abbr_pointer].isdigit():
      
      # Check for leading zero
      if abbr[abbr_pointer] == '0':
        return False
        
      # Capture entire numerical value
      start = abbr_pointer
    
      while abbr_pointer < len(abbr) and abbr[abbr_pointer].isdigit():
        abbr_pointer += 1
      
      # Convert numerical substring to an integer
      num = int(abbr[start:abbr_pointer])
      word_pointer += num
      
      # Check that we didn't exceed length of word
      if word_pointer > len(word):
        return False
        
    # If neither alphabetical or numerical scenario is satisfied
    else:
      return False

  # Check that we reached the end of the word
  if word_pointer != len(word):
    return False
  
  return True
  



def main():
    words = ["a", "a", "abcdefghijklmnopqrst", "abcdefghijklmnopqrst", "word", "internationalization", "localization"]
    abbreviations = ["a", "b", "a18t", "a19t", "w0rd", "i18n", "l12n"]

    for i in range(len(words)):
        print(i + 1, ".\t word: '", words[i], "'", sep="")
        print("\t abbr: ", abbreviations[i], "'", sep="")
        print(f"\n\t Is '{abbreviations[i]}' a valid abbreviation for the word '{words[i]}'? ", valid_word_abbreviation(words[i], abbreviations[i]), sep="")
        print("-" * 100)

if __name__ == '__main__':
    main()