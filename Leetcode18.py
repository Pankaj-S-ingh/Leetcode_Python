from typing import List
from numpy import sort


class Solution:
    def grpAnagram(self,strs:List[str])->List[List[str]]:
        dict={}
        for word in strs:
            sortedword="".join(sorted(word))
            if sortedword not in dict:
                dict[sortedword]=[word]
            else:
                dict[sortedword].append(word)

        result= []
        for item in dict.values():
                result.append(item)
        return result
print(Solution().grpAnagram(["eat","tea","tan","ate","nat","bat"]))