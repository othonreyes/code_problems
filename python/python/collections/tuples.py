def log(aTuple, level=1):
  print(type(aTuple))
  for i in aTuple:
    if isinstance(i, tuple):
      log(i, level + 2)
    else: 
      print('-' * level, i)

# set without nested elements
first = ('a' , 2, 'c')
log(first)

# set with nested elements
anotherTuple = (('a','b') ,(1,2))
log(anotherTuple)

# tuples with lists.
valid = (
    ['Mr John Smith      ', 13, 'Mr%20John%20Smith'],
    ['Mr Tata Smith      ', 13, 'Mr%20Tata%20Smith']
  )
log(valid)
# when a tuple has one or more values then they respect the value
for i in valid:
  print('i[',i,']=Mr John Smith      ', i[0] == 'Mr John Smith      ')

# tuple of one value
tupleOfOne = (['a'])
print(type(tupleOfOne)) # Prints <class 'list'> meaning is not a tuple even when it is declared as a tuple
print(type(tupleOfOne[0])) # Prints <class 'str'> which is the first element of the list

