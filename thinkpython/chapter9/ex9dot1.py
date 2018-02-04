def count():
  fin = open('words.txt', 'r')
  for line in fin:
    if len(line.strip()) > 20:
      print line.strip()

count()