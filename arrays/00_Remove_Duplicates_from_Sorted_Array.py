'''
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 
'''
pointer = 0
for i in range(len(nums)):
  if nums[i] != nums[pointer]:
    nums[pointer+1] = nums[i]
    pointer += 1
  elif nums[i] > nums[i-1]:
    break
return (pointer +1)
