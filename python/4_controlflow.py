# x = int(input("please enter a number"))
# if x < 0 :
#   print("negative number")
# elif x == 0:
#   print("zero")
# elif x == 1:
#   print("uno")
# else:
#   print("more")

# words = ['cat', 'dog', 'something']
# for w in words:
#   print(w, len(w))

# print('-'*10)
# for i in range(10):
#   print(i)

# print('-'*10)
# for i in range(10, 20):
#   print(i)

# print('-'*10)
# for i in range(10, 20, 2):
#   print(i)

# print('-'*10)
# for i in list(range(10, 20,5)):
#   print(i)

####  break and pass
# result = None
# for i in range(11, 30, 3):
#   if i % 5 == 0:
#     result = i
#     break
#   else:
#     continue
# print(f'result = {result}')

#### Functions
# def fib(n1, n0):
#   print(f'{n1}',end=',') 
#   if n1>=21:
#     return n1
#   return fib(n1+n0, n1)

# print(f'ib result: {fib(1,0)}')

### Default values
# def ask_ok(prompt, retries=4, reminder='Please try again'):
#   while True:
#     ok = input(prompt)
#     if ok in ('y', 'ye', 'yes'):
#       return True
#     if ok in ('n', 'no', 'nop'):
#       return False
#     retries = retries - 1
#     if retries < 0:
#       print('Invalid response')
#     print(reminder)

# ask_ok('Do you want to continue?')

### map and list of args
# def keys(address, *type, **rooms):
#   print(f'Do you live in {address}?')
#   print(f'Yes! I heard that the doors are made of ', end='')
#   for t in type:
#     print(f'{t}', end=', ')
#   print('And it has the rooms:')
#   print('-' * 20)
#   for kw in rooms:
#     print(kw, "------------", rooms[kw])

# keys('5934 123rd Ave SE',
#   'wood', 'metal', 'mud',
#   restroom = 'Family place',
#   bathroom = 'potty place',
#   yard = 'Pixie place'
# )

### Destructuring a list of arguments
def colors(red=None, blue=None, yellow=None):
  combinations = []
  if red is not None and blue is not None:
    combinations.append("Purple")
  if yellow is not None and blue is not None:
    combinations.append("Green")
  if red is not None and yellow is not None:
    combinations.append("Orange")
  if red is not None and yellow is not None and blue is not None:
    combinations.append("White")
  return combinations

some_colors = ['Red', 'Blue']
print(colors(*some_colors))

some_colors = { 'red' : 'Red', 'yellow' : True}
print(colors(**some_colors))

# Extending a list
nums1 = [1,2]
a = [].extend(nums1)
print("List extended ", a)
a = []
a.extend(nums1)
print("List extended ", a)
