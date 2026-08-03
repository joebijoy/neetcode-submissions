class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap ={}
        for index,value in enumerate(nums):
            ans = target - value
            if ans in hashmap:
                return [hashmap[ans], index]
            hashmap[value] = index
        return
            

            
            
        