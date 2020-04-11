
def powerset(aset, ix = 0):
  allsets = []
  if ix == len(allsets):
    allsets.append([])
  else:
    allsets = powerset(aset, ix + 1)
    item = aset[ix]
    for prev_set in allsets:
      new = prev_set.copy()
      new.append(item)
      allsets.append(new)
  return allsets

if __name__ == "__main__":
  aset = set([1,2,3])