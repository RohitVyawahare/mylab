def is_abecedarian(word):
  i = 0
  while i < len(word) - 1:
    if word[i] > word[i + 1]:
      return False
    i += 1
  return True

if __name__ == '__main__':
  print is_abecedarian('abcdc')