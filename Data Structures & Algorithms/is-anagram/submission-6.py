class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}

        for i in s:
            seen[i] = seen.get(i,0) + 1
        
        for i in t:
            if i in seen:
                seen[i] -= 1
                if seen[i] == 0:
                    del seen[i]
            else:
                return False
      
        if len(seen) == 0:
            return True
        else:
            return False 

        