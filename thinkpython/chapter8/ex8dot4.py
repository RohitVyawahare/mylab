def find(word, key, start):
  count = 0
  index = start
  while index < len(word):
    if word[index] == key:
      count = count + 1
    index += 1
  return count


print find('rohithihi', 'h', 0)

'''
OUTPUT:

pnq-rvyawahare:chapter8 $ python ex8dot4.py 
3

'''
