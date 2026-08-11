class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        

        for s in strs:
            keys = [0] * 26
            for c in s:
                keys[ord(c)-ord("a")] +=1
            res[tuple(keys)].append(s)
        
        return list(res.values())
                


        