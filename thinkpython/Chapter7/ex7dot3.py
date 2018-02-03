import ex7dot2
import math

i = 1.0

while i < 10:
  print ("> %f %f %f %f"%(i, ex7dot2.square_root(i), math.sqrt(i), abs(ex7dot2.square_root(i) - math.sqrt(i))))
  i = i + 1

