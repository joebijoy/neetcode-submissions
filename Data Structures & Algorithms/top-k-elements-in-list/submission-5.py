class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        freq = [[] for _ in range(len(nums)+1)]

        for n in nums:
            res[n] = res.get(n,0) + 1
        
        for key, value in res.items():
            freq[value].append(key)

        output = []
        for i in range(len(nums),-1,-1):
            for j in freq[i]:
                output.append(j)
                if len(output) == k:
                    return output
                    

        


            


        