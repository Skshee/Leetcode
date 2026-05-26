class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        Occurs = set()
        for num in nums:
            if(num in Occurs):
                return True
            else:
                Occurs.add(num)
        return False
    
# Smarter And Quicker Solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))