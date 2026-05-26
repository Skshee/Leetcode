'''
I have found 2 very small and simple ways to solve this problem : One is by using slicing and the other is pop() and insert.
Both of them can be solved in O(1)
'''

# Method 1
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums) 
        nums[:] = nums[-k:] + nums[:-k]  # Basically reverse first K and last K element and join them. That's the beauty of slicing :)

# Method 2
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            a=nums.pop()
            nums.insert(0,a) # Pop all values till K and add it to the end of the array and peace

        
        