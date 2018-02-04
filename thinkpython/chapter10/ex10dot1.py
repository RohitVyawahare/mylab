def nested_sum(l):
  lsum = 0
  for item in l:
    if type(item) is list:
      lsum = lsum + nested_sum(item)
    else:
      lsum = lsum + item  
  return lsum

if __name__ == '__main__':
  print nested_sum([1,2,3,[2,3,4,[1,[2,3]]]])