class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,n in enumerate(nums):
            match = target - n
            if match in hashmap:
                return [hashmap[match], i]
            hashmap[n] = i

        
            

            
            
        