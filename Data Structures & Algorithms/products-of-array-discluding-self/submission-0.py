class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_list = []
        length = len(nums)
        i = 0

        while i < length:
            product = 1
            for j in range(length):
                if i == j:
                    pass
                else:
                    product *= nums[j]
            product_list.append(product)
            i += 1
                    
        return product_list