my_set = set()
print('Empty set', my_set)

if my_set:
  print('Unexpected')
else:
  print('set is empty')

my_set.add(2)
print(my_set)
if 2 in my_set:
  print('set has a 2')