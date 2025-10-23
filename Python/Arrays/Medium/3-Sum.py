'''
Link : https://leetcode.com/problems/3sum/
Time Complexity : O(n^2)
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                if curr_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1
                    
                    # Skip duplicate values for 'b' and 'c'
                    # Move 'left' past any duplicates of the number just used.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Move 'right' past any duplicates of the number just used.
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif curr_sum > 0:
                    right -= 1
                else:
                    left += 1
            
        return res
