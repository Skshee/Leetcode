class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # We can't do product of all and divide by num as it will fail if a number is 0. So we use Prefix and Suffix product
        n = len(nums)
        answer = [1] * n
        
        # Step 1: Prefix product
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        
        # Step 2: Suffix product 
        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer