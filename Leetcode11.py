class Solution:
    def happyNum(self,n:int)->int:
        def sqsum(num):
            result=0
            while num>0:
                remender=num%10
                result+=pow(remender,2)
                num=num//10
            return result

        seen =set()
        while sqsum(n) not in seen:
            sum1=sqsum(n)
            if sum1==1:
                return True
            else:
                seen.add(sum1)
                n=sum1
        return False
print(Solution().happyNum(19)) 