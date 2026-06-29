class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans_dict = {}
        for i in nums:
            ans_dict[i] = ans_dict.get(i,0) + 1
        return sorted(ans_dict, key=ans_dict.get, reverse=True)[0:k]

        