'''
Link : https://leetcode.com/problems/4sum/
Time Complexity : O(n^3)
LeetCode Problem: 18. 4Sum
Difficulty: Medium
'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        answer = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                low = j+1
                high = n-1

                while low < high :
                    summ = nums[i] + nums[j] + nums[low] + nums[high]
                    if summ == target:
                        answer.append([nums[i],nums[j],nums[low],nums[high]])
                        low += 1
                        high -= 1
                        # IMP PART DON'T FORGET
                        while low < high and nums[low] == nums[low - 1]:
                            low += 1
                        while low < high and nums[high] == nums[high + 1]:
                            high -= 1
                    # ''''''''''''''''''''''''''''''''''''''''''''''''''''
                    elif summ < target:
                        low += 1
                    else:
                        high -= 1
        return answer


        
