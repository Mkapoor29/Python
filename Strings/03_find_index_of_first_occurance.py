haystack = "sadbutsad"
needle = "sad"
# method 1 -> find()
# return haystack.find(needle)

# method 2 -> implementation
for i in range(len(haystack)):
  if needle == haystack[i:i+len(needle)]:
    return i
return -1
