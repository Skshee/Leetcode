class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dic = {}
        ans = []

        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                dic[stack.pop()] = nums2[i]
            stack.append(nums2[i])

        for num in nums1:
            if(num not in dic.keys()):
                ans.append(-1)
            else:
                ans.append(dic[num])
        return ans

        


        
