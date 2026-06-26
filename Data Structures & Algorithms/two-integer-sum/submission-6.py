class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_list = []
        for i in range(len(nums)):
            for j in range(1,(len(nums))):
                if nums[i] + nums[j] == target and i != j:
                    index_list.append(i)
                    index_list.append(j)
                    return index_list



            
        