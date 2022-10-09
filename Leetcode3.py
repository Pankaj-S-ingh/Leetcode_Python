from itertools import count
from typing import List

#given an array of interger and an integer k ,you need to find
#the total number of continous subarray whose sum equals to k.
class Solution:
    def sumOfSubarray(self,nums:List[int],k:int)-> int:
        sumdict={0:1}
        s=0
        count=0
        for num in nums:
            s+=num
            if s-k in sumdict:
                count+=sumdict[s-k]
            if s in sumdict:
                sumdict[s]+=1
            else:
                sumdict[s]=1
        return count
print(Solution().sumOfSubarray([3,4,7,2,-3,1,4,2,1],7))