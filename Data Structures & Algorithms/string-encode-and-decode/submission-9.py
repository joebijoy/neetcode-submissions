class Solution:

    def encode(self, strs: List[str]) -> str:
        new_word = ""
        for i in strs:
            new_word += str(len(i)) + "#" + i
        return new_word

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s) - 1:
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            
            res.append(s[j+1:j+length+1])
            i = j+1+length
        return res

            

