class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output_list = []
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                output_list.append(left+1)
                output_list.append(right+1)
                return output_list

        

        