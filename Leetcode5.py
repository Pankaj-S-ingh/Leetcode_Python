class Solution:
    def strtoInt(self,s:str)->int:
        ns=s.strip()
        return int(ns)
x=Solution().strtoInt("   -67")
print(x,type(x))