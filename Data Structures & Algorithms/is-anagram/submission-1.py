class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = {}
        for i in s:
            res[i] = res.get(i,0) + 1
      
        for i in t:
            if i in res:
                res[i] -= 1
            if i not in res:
                return False
            if res[i] == 0:
                res.pop(i)
        if len(res) == 0:
            return True
        else:
            return False

        