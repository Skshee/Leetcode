class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        Counts = {}
        
        for char in 'balloon':
            Counts[char] = 0
        for char in text:
            if(char in 'balloon'):
                Counts[char] += 1
        Counts['l'] = Counts['l']//2
        Counts['o'] = Counts['o']//2
        # print(Counts)
        
        return min(Counts.values())