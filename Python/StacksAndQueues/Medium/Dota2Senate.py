'''
Link : https://leetcode.com/problems/dota2-senate/
Time Complexity : O(N)
Space Complexity : O(N)

Explanation : Using two queues to store the indices of Radiant and Dire senators.
n stores the total number of senators.Later, when senators get re-added for the next round, you’ll use n to assign new indices (since rounds loop cyclically).
'''
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        Rad = deque()
        Dir = deque()

        n = len(senate)

        for i in range(len(senate)):
            if senate[i] == 'R':
                Rad.append(i)
            else:
                Dir.append(i)

        while Rad and Dir:
            r = Rad.popleft()
            d = Dir.popleft()
            n += 1

            if r < d:
                Rad.append(n)
            else:
                Dir.append(n)

        return 'Radiant' if len(Dir) == 0 else 'Dire'