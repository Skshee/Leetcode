'''
Link : https://leetcode.com/problems/longest-subsequence-with-limited-sum/
'''
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()

        prefix = [0] * (len(nums) + 1)
        for i in range(1,len(nums)+1):
            prefix[i] = prefix[i-1] + nums[i-1] 

        print(prefix)

        answer = []

        for query in queries:
            count = 0
            for i in range(1, len(prefix)):
                if prefix[i] <= query:
                    count += 1
                else:
                    break
            answer.append(count)
        
        return answer
            

