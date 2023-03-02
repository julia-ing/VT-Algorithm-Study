from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)

        for word in strs:
            key = str(sorted(word))
            table[key].append(word)

        result = list(table.values())

        return result