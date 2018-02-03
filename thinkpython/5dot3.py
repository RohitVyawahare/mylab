def check_fermat(a, b, c, n):
  '''check if Fermat's theorm holds true'''
  if n < 2:
    print "Fermat's theorm holds true when n > 2"
  else: 
      if a**n + b**n == c**n:
        print "Holy smokes, fermat was wrong!"
      else:
        print "No, it doesn't work"
  return


def user_input():
  '''Take user input for a, b, c and n'''
  a, b, c, n = input("Enter values for a, b, c and n: ")
  check_fermat(a, b, c, n)

user_input()

''' OUTPUT:

pnq-rvyawahare:thinkpython rohit.vyawahare$ python 5dot3.py 
Enter values for a, b, c and n: 1,2,3,1
Fermat's theorm holds true when n > 2

pnq-rvyawahare:thinkpython rohit.vyawahare$ python 5dot3.py 
Enter values for a, b, c and n: 2,3,4,5
No, it doesn't work

'''



