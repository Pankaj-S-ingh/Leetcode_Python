

from typing import List


a=[1,2,3,4,5,6,72,3,2,1]
class Solution:
    def fun(self,length:int,a:List[int])->List[int]:
        b=set()
        for i in a:
            if a.count(i)>1:
                b.add(i)
        if len(b)==0:
            return [-1]
        else:
            return list(b)

print(Solution().fun(len(a),a))