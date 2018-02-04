def middle(l):
  trimmed_list = l
  trimmed_list.pop(0)
  trimmed_list.pop(len(l) - 1)
  return trimmed_list

if __name__ == '__main__':
  print middle([1,2,3,4,5])

