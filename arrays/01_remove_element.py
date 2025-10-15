nums = []
val = 2

while val in nums:
  nums.remove(val)
return len(nums)

for i in nums[:]:
  nums.remove(val)

nums = [x for x in num if x!= val]
