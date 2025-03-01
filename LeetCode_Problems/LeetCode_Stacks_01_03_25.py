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

# nums = [1,1,2]
#
# left = 0
# right = 1
#
# while(right < len(nums)):
#
#
#     if(nums[left] == nums[right]):
#         nums.pop(right)
#
#     else:
#         left+=1
#         right+=1
#
# print(len(nums))










# 80. Remove Duplicates From Sorted Array II

#
# nums = [0,0,1,1,1,1,2,3,3]
#
# left = 0
# right = 1
# r = False
#
# while(right < len(nums)):
#
#     if(r==False):
#         if(nums[left] == nums[right]):
#             r = True
#
#         left+=1
#         right+=1
#
#
#
#     if r ==True:
#         while(right<len(nums) and nums[left] == nums[right]):
#             nums.pop(right)
#         left+=1
#         right+=1
#         r=False
# print(len(nums))






















# 4. Median of Two Sorted Arrays

# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#
#         # Merge the two lists
#         nums1.extend(nums2)
#
#         # Sort the merged list (O(n log n) instead of O(n²))
#         nums1.sort()
#
#         n = len(nums1)
#
#         # Find the median
#         if n % 2 == 0:  # Even length
#             ty = n // 2
#             return (nums1[ty] + nums1[ty - 1]) / 2.0  # Return float
#
#         else:  # Odd length
#             ty = n // 2
#             return float(nums1[ty])  # Ensure float return type
#





