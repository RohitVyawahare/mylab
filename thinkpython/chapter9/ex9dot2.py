def has_no_e():
  
  count = 0
  total = 0

  f = open('words.txt', 'r')
  for line in f:
    word = line.strip()
    total += 1
    if 'e' not in word:
      print word
      count += 1

  print "Percentage of character e is %f"%(count/float(total))

has_no_e()