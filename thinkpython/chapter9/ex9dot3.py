def avoids(forbidden):
  
  f = open('words.txt', 'r')
  count = 0 

  for line in f:
    word = line.strip()
    i = 0
    while i < len(forbidden):
      if forbidden[i] in word: #if char in forbidden is found in word, break the loop
        break
      i = i + 1  
      if i == len(forbidden): #this means the char is not found in the word
        count = count + 1
        print word

  return count

print avoids('abcdfghijklnopqrstuvwx')

