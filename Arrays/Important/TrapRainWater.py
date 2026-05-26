'''
Link : https://leetcode.com/problems/trapping-rain-water/description/
Reference : https://www.youtube.com/watch?v=ZI2z5pq0TqA
Did the 2nd O(1) approach and honestly that even felt easier than the O(N) Approach
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxLeft = height[left]
        maxRight = height[right]
        count = 0

        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                count += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                count += maxRight - height[right]
        return count