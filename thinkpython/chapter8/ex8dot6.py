def find(word, key, start):
  
  count = 0
  index = start
  
  while index < len(word):
    if word[index] == key:
      count = count + 1
    index += 1
  return count

word = 'rohithihi'
key = 'h'
start = 0

print find(word, key, start)
print word.count('h', 0, len(word) - 2)

'''
OUTPUT:

pnq-rvyawahare:chapter8 $ python ex8dot4.py 
3

'''
