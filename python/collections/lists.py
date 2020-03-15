### Testing emptyness
list = None
if list:
  print("None lists shouldn't be printed")

if not list:
  print("None lists should be printed when negated")

list = []
if list:
  print("empty lists shouldn't be printed")
else:
  print("empty lists didn't was printed")

list = [None]
if list:
  print("Lists initialized with None are not empty")

list = [2]
if list:
  print("lists with items should be printed")

list = [2,3,4,5]
while list:
  val = list.pop(0)
  print("popping first element ", val)

list = [2,3,4,5]
while list:
  val = list.pop()
  print("popping last element", val)


list = [1, None, 3]
print(list)
while list:
  val = list.pop(0)
  print("popping last element", val)

list = []
list.append(None)
list.append(None)
while list:
  val = list.pop(0)
  print("popping last element", val)


# Nested matrixes
## Using multiplier / Wrong way
vertixes = 4
matrix = [[0] * vertixes] * vertixes
print(matrix)
## assign a value to the matrix
matrix[0][0] = 1
print(matrix)
## read a value from the matrix
var = matrix[0][0]
print(var)
## Using the right way with list comprehension
matrix = [[0 for i in range(vertixes)] for j in range(vertixes)]
matrix[0][0] = 1
print(matrix)