'''
Link: https://leetcode.com/problems/detonate-the-maximum-bombs/
Reference : https://www.youtube.com/watch?v=8NPbAvVXKR4
Company : Google
'''

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i in range(len(bombs)):
            for j in range(i+1, len(bombs)):
                x1,x2 = bombs[i][0], bombs[j][0]
                y1,y2 = bombs[i][1], bombs[j][1]
                d = (((x1-x2)**2 + (y1 - y2)**2)**(1/2))

                r1,r2 = bombs[i][2], bombs[j][2]

                if d <= r1:
                    graph[i].append(j)

                if d <= r2:
                    graph[j].append(i)
        res = 0

        def dfs(i,visit):  
        # For each bomb, we simulate a detonation and count how many bombs can go off using DFS.
        # A new visited set ensures each run is independent, like restarting the whole setup.
            if i in visit:
                return 0
            visit.add(i)
            count = 1
            for neighbour in graph[i]:
                count += dfs(neighbour,visit)
            return count

        for i in range(len(bombs)):
            visit = set()
            res = max(res,dfs(i, visit))
        return res
