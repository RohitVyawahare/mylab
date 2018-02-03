
import math

def factorial(n):
  fact = 1
  for i in range(1, n + 1):
    fact = fact * i
  return fact

def calculate_pi():

  k = 0
  summation = 0
  val = 1
  t = ((2 * math.sqrt(2)) / 9801) 

  while val > 1e-15:
    num = factorial(4 * k) * (1103.0 + 26390 * k)
    den = (factorial(k) ** 4) * (396.0 ** (4 * k))
    val = t * (num / den)
    k = k + 1
    summation = summation + val
   
  print "Value of pi: %f"%(1 / summation)

calculate_pi()

'''
OUTPUT:

pnq-rvyawahare:Chapter7 rohit.vyawahare$ python  ex7dot5.py 
Value of pi: 3.141593

'''