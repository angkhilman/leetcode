from collections import defaultdict

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        d1 = defaultdict(int)
        for i in words1:
            d1[i] += 1
        d2 = defaultdict(int)
        for i in words2:
            d2[i] += 1
        s1 = [i for i in d1 if d1[i] == 1]
        s2 = [i for i in d2 if d2[i] == 1]
        ans = set(s1).intersection(s2)
        return len(ans)
        
