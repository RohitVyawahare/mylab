def is_triange(a, b, c):
  '''takes three integers as arguments and checks if the triange can be formed or not'''
  if a + b > c and b + c > a and a + c > b:
    print "Triange can be formed!"
  else:
    print "Triange can not be formed."

  return


a, b, c = input("Enter sides of triange: ")
is_triange(int(a), int(b), int(c))

'''
OUTPUT:
pnq-rvyawahare:thinkpython rohit.vyawahare$ python 5dot4.py 
Enter sides of triange: 1,2,3
Triange can not be formed!

pnq-rvyawahare:thinkpython rohit.vyawahare$ python 5dot4.py 
Enter sides of triange: 3,3,4
Triange can be formed!

pnq-rvyawahare:thinkpython rohit.vyawahare$ python 5dot4.py 
Enter sides of triange: 100,1,1
Triange can not be formed!
'''



