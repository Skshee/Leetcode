'''
Link : https://leetcode.com/problems/subsets/
Similar to Permutations, but we add all subsets including empty set.
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, index):
            if index > len(nums):
                return

            ans.append(curr[:])

            for j in range(index, len(nums)):
                curr.append(nums[j])
                backtrack(curr, j+1)
                curr.pop()

        ans = []
        backtrack([], 0)
        return ans