'''
 Okay so we're given that each array withing the 2D array has only *distict* positive integers. This means that if a number is present in each array, it's count must be equal to length of the 2D array (n).
'''
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        counts = {} # A hashmap can be used to basically count occurence of each number in the 2D array
        ans = []
        for arr in nums:
            for num in arr:
                if (num not in counts):
                    counts[num]=1
                else:
                    counts[num]+=1
            
        for key in counts:
            if (counts[key] == n):
                ans.append(key)
        return sorted(ans)