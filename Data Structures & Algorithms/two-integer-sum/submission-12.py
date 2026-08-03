class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for index, value in enumerate(nums):
            second = target - value
            if second in hash_map:
                return [hash_map[second], index]
            hash_map[value] = index
        
        
            

            
            
        