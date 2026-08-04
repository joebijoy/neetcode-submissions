class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for _ in range(len(nums)+1)]

        for n in nums:
            count[n] = count.get(n,0) + 1
        for key, value in count.items():
            frequency[value].append(key)
        
        res = []
        for i in range(len(nums),0,-1):
            for n in frequency[i]:
                res.append(n)
                if len(res) == k:
                    return res
        