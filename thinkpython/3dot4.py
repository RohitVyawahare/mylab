def do_twice(f, s):
  f(s)
  f(s)

def print_twice(s):
  print s

do_twice(print_twice, 'rohit')
do_twice(print_twice, 'mrunal')

'''
OUTPUT:

pnq-rvyawahare:thinkpython rohit.vyawahare$ python 3dot4.py 
rohit
rohit
mrunal
mrunal

'''

