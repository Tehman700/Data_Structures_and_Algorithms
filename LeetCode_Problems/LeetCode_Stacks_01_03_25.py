# 2460. Apply Operations to an Array
from colorsys import rgb_to_hls

# nums = [1,0,2,0,0,1]
# left = 0
# right = left+1
# t = 0
#
# for i in range(len(nums) -1):
#
#     first = nums[left]
#     sec = nums[right]
#
#     if(first == sec):
#         nums[left] = nums[left] * 2
#         nums[right] = 0
#
#     left+=1
#     right+=1
# print(nums)
#
# for i in nums[:]:
#     if(i == 0):
#         nums.remove(i)
#         t+=1
#
# for _ in range(t):
#     nums.append(0)
#
# print(nums)

















# 26. Remove Duplicates from Sorted Array

nums = [1,1,2]

left = 0
right = 1

while(right < len(nums)):


    if(nums[left] == nums[right]):
        nums.pop(right)

    else:
        left+=1
        right+=1

print(len(nums))









