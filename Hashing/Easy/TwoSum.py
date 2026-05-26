# Basically store all nums in dictionary as keys and their indices as values. If complement(target - num) already belongs in the dict then return the indices in the dict. Faster than bruteforce - O(1) compared to O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if (complement in dic):
                return [i,dic[complement]]
            dic[nums[i]]=i
        return [-1,-1]