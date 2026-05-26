'''
Link : https://leetcode.com/problems/find-lucky-integer-in-an-array/description/?envType=problem-list-v2&envId=ajcqwr0m
'''

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = {}
        luckyNums = []
        for num in arr:
            if(num not in counts):
                counts[num]=1
            else:
                counts[num]+=1
        for num,freq in counts.items():
            if(freq == num):
                luckyNums.append(num)
        if(len(luckyNums)== 0):
            return -1
        else:
            return max(luckyNums)