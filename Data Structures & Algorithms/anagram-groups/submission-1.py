from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # Mapping CharCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # count each letter a..z

            for c in s:
                count[ord(c) - ord("a")] += 1 #Map out each asci value letter
        
            result[tuple(count)].append(s)
        
        return list(result.values()) # O( m * n) m = length of List and n = avg length of a string