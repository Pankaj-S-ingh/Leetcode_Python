class Solution:
    def largestpalindromicSubString(self,s:str)->str:
        res=""
        for i in range(len(s)):
            #"abbba"
            odd= self.helper(s,i,i)
            #"abba"
            even=self.helper(s,i,i+1)
            res=max(odd,even,res,key=len)
        return res

    def helper(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]

print(Solution().largestpalindromicSubString("nitin"))