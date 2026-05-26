'''
Link to question : https://leetcode.com/problems/contiguous-array/
A very good question that covers prefix_sum (but not in a summation kinda way) and also using hash maps
Reference : https://www.youtube.com/watch?v=agB1LyObUNE
'''
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zeros = 0
        ones = 0
        res = 0
        diff = {} # Stores the diff b/w count[1] - count[0] for each index
        for i,num in enumerate(nums):
            if (num == 0):
                zeros += 1
            if (num == 1):
                ones += 1
                
            if((ones - zeros)not in diff):   # When number of one's and zeros are equal from index 0 to i, diff will be 0 but this case won't be captured correctly
                diff[(ones - zeros)] = i 
            
            if(ones == zeros):
                res = ones + zeros 
            else:
                Index = diff[(ones - zeros)]
                res = max(res,i-Index) # I didn't do i - Index and was stuck for sooo longgg
            
        return res
        
