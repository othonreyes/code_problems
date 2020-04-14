#define a dictionary
my_dict = {}
print("Empty dict ", my_dict)

# Assign a value to a dict
my_dict[str(5)] = "My value"
print("dict with a value ", my_dict)

# check if a value is in the dict
if str(5) in my_dict:
  print("dict has the value 5 ")

# check if a value is not in the dict
if str(1) not in my_dict:
  print("dict doens't have the value 1")

my_dict["k1"] = "v1"
my_dict["k2"] = "v2"
my_dict["k3"] = "v3"

# Iterating over a dic's keys
for i in my_dict:
  print("Key ", i)

# Iterating over a dic's values
for i in my_dict.values():
  print("Value ", i)

# Iterating over a dic's keys and values
for key, value in my_dict.items():
  print("K: {} = {}".format(key, value))

# erase an item
del my_dict["k1"]
print("dict without k1 ", my_dict)

# Initializing a dic using list comprehension
dist = dict([ (str(i), 1000) for i in range(5)])
print("dict without k1 ", dist)

# dict to list
## verbose way
a = []
for i,j in dist.items():
  a.append(i + "-" + str(j) )
print(",".join(a))

## idiomatic way
a = [ k +" " + str(dist[k]) for k in dist.keys() ]
print(",".join(a))

# list to dict
a = [1,2,3]

## verbose way
dist = {}
for i in a:
  dist[i] = i
print(dist)

## dict comprehension
dist = {x: x for x in a}
print(dist)


cpdomains = ["9001 discuss.leetcode.com"]
domains = {j[1]:j[0] for j in [i.split(" ") for i in cpdomains] }
print(domains)