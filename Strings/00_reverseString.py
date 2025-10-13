s = "hello"

# method 1 -> slicing
s[:] = s[::-1]

# method 2 -> two-pointer approach
start = 0
end = len(s) - 1
for i in range(len(s)):
  s[start], s[end] = s[end], s[start]
  start += 1
  end  -=1
  if(end<start):
    break
