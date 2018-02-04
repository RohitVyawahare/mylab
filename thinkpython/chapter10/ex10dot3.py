def cumulative_sum(l):
  
  i = 1
  cl = []
  cl.append(l[0])
  
  while i < len(l):
    cl.append(l[i] + cl[i-1])
    i = i + 1
  
  return cl

if __name__ == '__main__':
  print cumulative_sum([1, 2, 3, 4])

'''
OUTPUT:

pnq-rvyawahare:chapter10 rohit.vyawahare$ python ex10dot3.py 
[1, 3, 6, 10]

'''