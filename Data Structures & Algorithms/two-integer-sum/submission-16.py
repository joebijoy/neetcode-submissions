class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i,n in enumerate(nums):
            find = target - n
            if find in hash_map:
                return [hash_map[find], i]
            else:
                hash_map[n] = i

        