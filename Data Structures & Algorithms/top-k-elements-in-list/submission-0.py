class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for i in nums:
            nums_dict[i] = 0
        for i in nums:
            if i in nums_dict.keys():
                nums_dict[i] += 1
        count = k
        output_list = []
        while count != 0:
            max_key = max(nums_dict, key=nums_dict.get)
            output_list.append(max_key)
            nums_dict.pop(max_key)
            count -= 1
        return output_list
                