def createNewWords(length_of_letter,number_of_new_words):
  import random as rd
  vowels = "aeıioöuü"
  consonants= "qwrtypğsdfghjklşzxcvbnmç"
  start_vowel = False
  new_words_array = []

  for i in range(number_of_new_words):
    new_word = ""
    start_vowel = True if rd.randint(0,1) == 0 else False
    if not start_vowel:
      for i in range(length_of_letter):
        if i %2 == 0:
          new_word += consonants[rd.randint(0,len(consonants)-1)]
        else:
          new_word += vowels[rd.randint(0,len(vowels)-1)]
    else:
      for i in range(length_of_letter):
        if i %2 == 0:
          new_word += vowels[rd.randint(0,len(vowels)-1)]
        else:
          new_word += consonants[rd.randint(0,len(consonants)-1)]
    new_words_array.append(new_word)
  return new_words_array
print(createNewWords(length_of_letter=6,number_of_new_words=20))