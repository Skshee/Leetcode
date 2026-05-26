'''
Link : https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals
'''

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = defaultdict(int)

        for num in arr:
            freq[num] += 1
        
        ordered = sorted(freq.values())
        
        idx = 0
        while k > 0 and idx < len(ordered):
            if k >= ordered[idx]:
                k -= ordered[idx]
                idx += 1
            else:
                break
        
        return len(ordered) - idx

            
            