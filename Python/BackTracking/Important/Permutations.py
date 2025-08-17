'''
Link : https://leetcode.com/problems/permutations/
Method : Backtracking
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()
        
        ans = []
        backtrack([])
        return ans
    
'''
Visual Representation
[]
├── [1]
│   ├── [1,2]
│   │   └── [1,2,3] ✅
│   └── [1,3]
│       └── [1,3,2] ✅
├── [2]
│   ├── [2,1]
│   │   └── [2,1,3] ✅
│   └── [2,3]
│       └── [2,3,1] ✅
└── [3]
    ├── [3,1]
    │   └── [3,1,2] ✅
    └── [3,2]
        └── [3,2,1] ✅

'''