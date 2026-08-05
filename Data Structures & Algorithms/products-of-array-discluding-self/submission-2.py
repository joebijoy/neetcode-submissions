class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        self_dict = {}
        for i,n in enumerate(nums):
            index = 0    
            self_dict[i] = self_dict.get(i,0) + 1
            while index < len(nums):
                if index == i:
                    index += 1
                else:
                    self_dict[i] *= nums[index]
                    index += 1
        res = []
        for i in self_dict.values():
            res.append(i)
        return res


