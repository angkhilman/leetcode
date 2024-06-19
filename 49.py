import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            sorted_i = ''.join(sorted(list(i)))
            d[sorted_i].append(i)
        answer = []
        for k in d:
            answer.append(d[k])
        return answer
        
