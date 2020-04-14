def mult(x,y):
  if y == 0:
    return 0
  if y == 1:
    return x
  newY = y >> 1
  r = mult(x, newY)
  if y % 2 == 0:
    return r + r
  else:
    return r + r + x

if __name__ == "__main__":
  print(mult(5,10))
