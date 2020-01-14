## Didn't work
def tobinary(xcopy):
  bn=""
  while (xcopy >= 0):

    if xcopy%2 == 0:
      temp = xcopy//2
      xcopy -= 2
      bn += str(temp)
    else:
      temp = xcopy % 2
      xcopy -= temp
      bn += str(temp)
  return bn

# 0 = 0
# 1 = 1
# 2 = 10
# 2 % 2 = 0
# 2/2 = 1
#   =     = / = %
# 1 =   1 = 0 = 1 - 
# 2 =  10 = 0 = 0  
# 3 =  11 = 1 = 1
# 4 = 100 = 2 = 0
# 5 = 101 = 2 = 1

# result = "1" * (number/2) + number % 2


## Key take away was that it is important to learn techniques
## here they kwy was to learn how to break the number of the digits for the
# target base
for i in range(0,5):
  result = ""
  
  copy = i
  while copy > 1:
    temp = copy//2    
    result += str(temp % 2)
    copy = temp
  print("number " + str(i) + " is " + result)
