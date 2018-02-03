import sys

def square_root(a):
  ''' y = x + (a / x)/2'''
  x = 0
  y = 1

  while abs(y - x) > sys.float_info.epsilon:
    x = y
    y = (x + (a / x)) / 2.0
    print "x: %f, y: %f"%(x, y)
  
  return y

if __name__ == '__main__':
  print square_root(64)
  print square_root(62)

'''
OUPUT:

pnq-rvyawahare:thinkpython rohit.vyawahare$ python 7dot2.py 
x: 1.000000, y: 32.500000
x: 32.500000, y: 17.234615
x: 17.234615, y: 10.474036
x: 10.474036, y: 8.292192
x: 8.292192, y: 8.005148
x: 8.005148, y: 8.000002
x: 8.000002, y: 8.000000
x: 8.000000, y: 8.000000
x: 8.000000, y: 8.000000
8.0
x: 1.000000, y: 31.500000
x: 31.500000, y: 16.734127
x: 16.734127, y: 10.219565
x: 10.219565, y: 8.143180
x: 8.143180, y: 7.878457
x: 7.878457, y: 7.874009
x: 7.874009, y: 7.874008
x: 7.874008, y: 7.874008
x: 7.874008, y: 7.874008
7.87400787401

'''