class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""
        for i in strs:
            word += str(len(i)) + "#" + i
        return word
     

    def decode(self, s: str) -> List[str]:
        doc_list = []
        i=0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            word_length = int(s[i:j])
            word = s[j+1: j+1+word_length]
            doc_list.append(word)
            i = j+1+word_length
        return doc_list
    

