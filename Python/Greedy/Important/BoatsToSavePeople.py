'''
Link: https://leetcode.com/problems/boats-to-save-people/

Pair the lightest and heaviest person whenever possible; if they fit within the limit, move both pointers, otherwise send the heavier one alone.
Each step uses one boat until everyone is assigned.
'''
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        i = 0
        j = n - 1
        people.sort()
        ans = 0

        while i <= j:
            if people[i] + people[j] <= limit: # If lightest and heaviest can share a boat
                i += 1  # lightest person gets on the boat

            j -= 1  # heaviest person always gets on the boat
            ans += 1
        return ans