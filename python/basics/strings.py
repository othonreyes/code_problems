s = "Hey there! what should this string be?"
# Length should be 20
print("Length of s = %d" % len(s[0:20]))

# Index
print("The first occurrence of the letter a = %d" % s.index("!"))

# Count
print("t occurs %d times" % s.count("t"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end
print("Reverse the characteres are '%s'" % s[::-1]) # string reversed
print("Reverse the characteres are '%s'" % s[::-2]) # reversed with odd index

# uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
print("String starts with 'Str'.!", s.startswith("Str"))

# Check how a string ends
print("String ends with 'ome!'.!", s.endswith("ome!"))

# Split
print("Split the words of the string: %s" % s.split(" "))