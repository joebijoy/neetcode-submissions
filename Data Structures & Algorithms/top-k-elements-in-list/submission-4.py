class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       count = {}
       freq = [[] for _ in range(len(nums)+1)]

       for i in nums:
        count[i] = count.get(i,0) + 1
       for key, value in count.items():
        freq[value].append(key)
       res = []
       for i in range(len(nums),0,-1):
        for n in freq[i]:
            res.append(n)
        if len(res) == k:
            return res


        