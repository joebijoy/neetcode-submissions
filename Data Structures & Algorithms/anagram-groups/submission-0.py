class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_list = []
        for i in strs:
            empty_list = []
            for j in strs:
                if sorted(list(j)) == sorted(list(i)):
                    empty_list.append(j)
            if empty_list not in output_list:
                output_list.append(empty_list)
      
            
        
        return output_list


        