def is_power(a, b):
  if a % b == 0:
    return is_power(a/b, b)
  else:
    if a > b:
      return False
    else:
      return True

print is_power(128,2)