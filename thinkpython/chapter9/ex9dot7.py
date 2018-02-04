def three_consecutive():
  fh = open('words.txt', 'r')
  for line in fh:
    word = line.strip()
    i = 0
    count = 0
    while i < len(word) - 1:
      if word[i] == word[i + 1]:
        i = i + 2
        count = count + 1
        if count == 3:
          print word
      else:
        i = i + 1
        count = 0
  return

if __name__ == '__main__':
  three_consecutive()  
