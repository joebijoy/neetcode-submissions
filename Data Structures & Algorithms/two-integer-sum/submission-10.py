class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        res_list = []
        for i,n in enumerate(nums):
            if target - n in res:
                res_list.append(res[target-n])
                res_list.append(i)  
            else:
                res[n] = i
        return res_list
        


            
        