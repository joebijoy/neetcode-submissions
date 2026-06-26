class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_list = []
        for i in nums:
            if i in duplicate_list:
                return True
            duplicate_list.append(i)
        return False
            
        
        