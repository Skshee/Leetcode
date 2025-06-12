class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        source = set()
        dest = set()
        for path in paths:
            source.add(path[0])
            dest.add(path[1])
        
        for city in dest:
            if city not in source:
                return city
        return None
