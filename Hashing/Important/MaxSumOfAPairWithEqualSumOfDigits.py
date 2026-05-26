'''
Link : https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/description/

We'll be using a dictionary whose keys will be the digit sum and it's values will be the numbers whose digits add add up to the key's value
'''

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum = {}
        max_sum = -1
        for i,num in enumerate(nums):
            num_original = num
            Sum = 0
            while num>0:
                Sum += num % 10
                num = num//10
            
            if (Sum not in digit_sum):
                digit_sum[Sum] = []

            digit_sum[Sum].append(num_original)
        print(digit_sum)
        
        for num_list in digit_sum.values(): # Iterating over the values of the dict which is basically the list of numbers for each digit sum
            if(len(num_list)>=2):
                num_list.sort(reverse=True) #For Getting the 2 highest nums
                pair_Sum = num_list[0]+num_list[1] # Adding the 2 highest nums
                max_sum = max(max_sum, pair_Sum)
        return max_sum
