vector = 0
char = 'a'
print('Original vector ', vector)
# set the vector
# 1 first get the position int
charInt = ord(char)
print(char,' ', charInt)
# rest the first charcter so we don't overflow
charInt = charInt - ord('a')
# Then place a bit '1' in the given position by moving 1 'n' positions to the left. We do this by doing an 'OR' operation
vector = (1<<charInt)
print('Final vector ', vector)

# Let's use it to compare
# To do that we do an 'AND' operation with a '1' moved 'n' positions to the left.
result = True if vector & (1<<charInt) else False
print('Do you have an \'a\'? ', result)