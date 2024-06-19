from collections import defaultdict
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count1 = defaultdict(int)
        count2 = defaultdict(int)
        
        for word in words1:
            count1[word] += 1
            
        for word in words2:
            count2[word] += 1
        
        unique1 = {word for word in count1 if count1[word] == 1}
        unique2 = {word for word in count2 if count2[word] == 1}
        
        common_unique_words = unique1.intersection(unique2)
        
        return len(common_unique_words)
