def do_twice(f, s):
  f(s)
  f(s)

def do_four(f,s):
  do_twice(print_twice, s)
  do_twice(print_twice, s)

def print_twice(s):
  print s

do_four(print_twice, 'rohit')


