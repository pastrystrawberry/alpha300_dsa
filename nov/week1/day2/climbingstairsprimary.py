class Solution:
    def h(self,n:int,mp:dict[int,int])->int:
        if n==0 or n==1:
            return 1
        if n not in mp:
            mp[n]=self.h(n-1,mp)+self.h(n-2,mp)
        return mp[n]
    def climbStairs(self, n: int) -> int:
        mp={}
        return self.h(n,mp)        