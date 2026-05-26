'''
Link : https://leetcode.com/problems/frequency-of-the-most-frequent-element/
Reference : https://www.youtube.com/watch?v=vgBrQ0NM5vE
Companies : Meta
Topic : Arrays, Sliding Window, Sorting, Prefix Sum
Time Complexity : O(n log n) due to sorting
'''

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort the array to use a sliding window approach
        res, total = 0, 0  
        left, right = 0, 0  

        while right < len(nums):
            total += nums[right]  # Add current element to window sum

            # If we need more than k increments to make all elements equal to nums[right],
            # shrink the window from the left
            if nums[right] * (right - left + 1) > total + k:
                # Sliding the window
                total -= nums[left]  
                left += 1  

            res = max(res, right - left + 1)
            right += 1  
        
        return res 
