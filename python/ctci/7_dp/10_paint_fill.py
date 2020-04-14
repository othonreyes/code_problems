def paintFill(p, x, y, old, new):
  r = len(picture)
  c = len(picture[0])
  paint(p, x, y, r, c, old, new)

def paint(p, x, y, r, c, old, new):
  if x < 0 or y < 0 or x == c or y == r:
    return
  if p[y][x] != old or p[y][x] == new:
    return
  p[y][x] = new
  paint(p, x - 1, y - 1, r, c, old, new)
  paint(p, x, y - 1, r, c,old, new)
  paint(p, x + 1, y - 1, r, c, old, new)
  paint(p, x - 1, y, r, c, old, new)
  paint(p, x + 1, y, r, c, old, new)
  paint(p, x - 1, y + 1, r, c, old, new)
  paint(p, x, y + 1, r, c, old, new)
  paint(p, x + 1, y + 1, r, c, old, new)

if __name__ == "__main__":
  picture = [
    [0,1,0,1,0,1,0,1,0],
    [0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,1,1],
    [0,0,1,0,0,0,0,1,1],
  ]

  result = [
    [2,1,2,1,0,1,2,1,2],
    [2,2,2,1,1,1,2,2,2],
    [2,2,2,2,2,2,2,2,2],
    [2,2,1,2,2,2,2,1,1],
    [2,2,1,2,2,2,2,1,1],
  ]

  paintFill(picture, 5,2,0,2)

  r = len(picture)
  c = len(picture[0])

  for i in range(r):
    print(picture[i])

  for i in range(r):
    for j in range(c):
      assert picture[i][j] == result[i][j]