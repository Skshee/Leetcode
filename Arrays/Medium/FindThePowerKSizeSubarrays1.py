'''
Link : https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/
Time Complexity : O(n*k)
'''
class Solution:
    def isSorted(self, arr):
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] != 1: # Consecutively increasing
                return False
        return True

    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        left = 0
        ans = []

        while left < len(nums) - k + 1:
            window = []
            
            for i in range(k):
                window.append(nums[left + i])

            if self.isSorted(window):
                ans.append(window[-1])
            else:
                ans.append(-1)

            left += 1
        
        return ans
            
