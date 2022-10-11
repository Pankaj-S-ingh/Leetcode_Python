from re import L
from typing import List


class Solution:
    def maxsumSubArray(self,nums:List[int])->int:
        total_num=max_num=nums[0]
        for i  in nums[1:]:
            total_num=max(i,total_num+i)
            max_num=max(total_num,max_num)
        return(max_num)
print(Solution().maxsumSubArray([-2,1,-3,4,-1,2,1,-5,4]))