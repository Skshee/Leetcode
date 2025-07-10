'''
Link : https://leetcode.com/problems/minimum-genetic-mutation/
'''

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1

        def diff(gene1,gene2):
            count = 0
            for i in range(len(gene1)):
                if gene1[i] != gene2[i]:
                    count += 1
            return count

        queue = deque()
        visit = set()
        queue.append([startGene, 0])
        visit.add(startGene)

        while queue:
            gene, mutations = queue.popleft()

            if gene == endGene:
                return mutations

            for newGene in bank:
                if newGene not in visit and diff(gene, newGene) == 1:
                    queue.append([newGene, mutations + 1])
                    visit.add(newGene)
        return -1

        