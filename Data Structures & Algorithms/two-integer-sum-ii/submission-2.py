class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output_list = []
        first = 0
        second = 1
        length = len(numbers)  
        while first < length:
            while second < length:
                if numbers[first] + numbers[second] == target:
                    output_list.append(first+1)
                    output_list.append(second+1)
                    return output_list
                second += 1
            second = 1
            first += 1
        

        