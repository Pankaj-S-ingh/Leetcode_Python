# Roman to integer number;


class Solution:
    def RomanIntoIneger(self,s:str)->int:
        dic={'I':1,
             'V':5,
             'X':10,
             'L':50,
             'C':100,
             'D':500,
             'M':1000}
        current=0
        prev=0
        total=0
        for i in range(len(s)):
            current=dic[s[i]]
            if prev<current:
                total+=current-(2*prev)
            else:
                total+=current
            prev=current
        return total
print(Solution().RomanIntoIneger('XLIX'))