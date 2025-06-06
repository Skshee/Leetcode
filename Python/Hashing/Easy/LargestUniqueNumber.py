'''
Basically store each num and it's frequency in a dictionary and return the maximum num where freq = 1
'''

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        Occurence = {}
        lst = []
        for num in nums:
            if(num not in Occurence):
                Occurence[num]=1
            else:
                Occurence[num]+=1
        for num,freq in Occurence.items(): # Was stuck here because I forgot to use .items()
            if freq == 1:
                lst.append(num)
        if(len(lst)==0):
            return -1
        else:
            return max(lst)