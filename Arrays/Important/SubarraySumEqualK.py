'''

This question combines both Prefix Sum and Hashmap approach
- We're initially storing the key:value pair of 0:1 in a dictionary
- As we iterate, we maintain a running sum (prefix_sum) and check if (prefix_sum - k) is present in the dict
- If it's present we add the value to the Count variable which is initially 0
- Then we add the prefix_sum ka value to the dict

'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        Dic = {0:1}
        n = len(nums)
        prefix_sum = 0
        Count = 0
        for i in range(n):
            prefix_sum += nums[i]
            if(prefix_sum - k in Dic):
                Count += Dic[prefix_sum - k]
            if(prefix_sum not in Dic):
                Dic[prefix_sum] = 1
            else:
                Dic[prefix_sum] += 1
        return Count
        