'''
Link : https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/description/?envType=daily-question&envId=2025-06-18
Question Of The Day : 18/6/25
Asked by : Google 
'''

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(0,len(nums)-2,3):
            if(nums[i+2] - nums[i]) > k:
                return []
            else:
                ans.append(nums[i:i+3])
        return ans