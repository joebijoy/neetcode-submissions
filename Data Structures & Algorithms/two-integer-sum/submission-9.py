class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        res_list = []
        for i,n in enumerate(nums):
            if target - n in res:
                res_list.append(i)
                res_list.append(res[target-n])
            else:
                res[n] = i
        return sorted(res_list)
        


            
        