'''
Thought of logic correctly but had to learn new things in syntax that's why put in important
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Okay so if 2 strings are anagrams, then when they are sorted they will be in the same order and yes strings can be sorted using sorted() as it return a new string
        groups = {}
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if (sorted_string not in groups):
                groups[sorted_string] = []

            groups[sorted_string].append(string)
        return list(groups.values())
