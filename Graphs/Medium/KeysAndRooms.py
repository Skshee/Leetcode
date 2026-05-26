'''
Link : https://leetcode.com/problems/keys-and-rooms/
'''

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(i):
            for key in rooms[i]:
                if key not in visited:
                    visited.add(key)
                    dfs(key)
        
        visited = set()
        visited.add(0)
        dfs(0)
        return len(rooms) == len(visited)
        
        
                
        
        
                