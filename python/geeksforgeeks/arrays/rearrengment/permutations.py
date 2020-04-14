## Generate the possible permutations of a string
# Below are the permutations of string ABC.
# ABC ACB BAC BCA CBA CAB
# [A][B][C]
# [A][C][B]
# ---
# [B][A][C]
# [B][C][A]
# ---
# [C][A][B]
# [C][B][A]


# option 1: create a list of the chars, then 
# create a sublist that is the difference of the original list
# the chars used. Take the first charcter and append it.
# Create a new sublist of the charcters not used.
# and repeat the process
# Summary:
# This alorithm works by iterating over a set with the input and recursively creating subsets 
# excluding the char we are iterating over.
# Time: O(n^2)
# Space: ???

# Description:
# The key in this algortihm is to think about the input as sets. We iterate over the elements
# and track which char we are using then obtain a new set that excludes this item. When the subset 
# is emtpy then we add it to the list of results.

# The beauty of creating the subsets excluding the element that we know is that creates a
# 'Tracking' effect on the algorithm. It is like saying "Create a new set but don't use the one
# that I know". This 'Tracking' effect is nice becasue that way we don't repeat the element in use.

# If the set that we are iterating is s1 and the item that we are working is 'char' then the difference is 
# sdiff = s1 - char
# Example:
# s1 = {'A','B','C'}
# char = 'A'
# sdiff = s1 - char = {'B','C'}
  
def fact(n):
  if n == 1:
    return n
  return n * fact(n-1)

input='ABC'
inputSet = set(input)
n = len(inputSet)
total_options = fact(n)
print('Total possible options ',total_options)

result = set()
newString=''


def permutationsLessMemory(input, n):
  a=list(input)
  permute(a,0, n)

# It is using backtracking to do the permutations. they key thing here is that we backtrack by
# moving the start index to the right to iterate over the arrar.
# The permutations are created by swaping the elements of the array. We swap the first time
# to make a permutation, the second time is to revert the swap
def permute(a, start, end):
  if start == end-1:
    print(a)
    return
  for i in range(start, end):
    a[start],a[i] = a[i],a[start] 
    permute(a, start+1, end)
    a[start],a[i] = a[i],a[start]

def permutations(input):
  results=set()
  s1=set(input)
  combinations(s1,results,'')
  return results


def combinations(s1,results,newStr):
  for i in s1:
    # newStr+=char    this is accumulating the chars that we are iterating
    char = i
    sdiff = s1.difference(set(i))
    if len(sdiff) == 0:
      results.add(newStr+char)
    else:
      combinations(sdiff,results,newStr+char)


result = permutations(input)
print('Total possible options ', result)
permutationsLessMemory(input, n)