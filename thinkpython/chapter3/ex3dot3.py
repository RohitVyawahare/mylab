def right_justify(s):
  '''takes string named s as parameter and prints the string with enough leading
  spaces so that the last letter of the string in in col 70 of the display'''
  print (" " * (70 - len(s)) + s)

right_justify('rohit')
right_justify('vyawahare')
