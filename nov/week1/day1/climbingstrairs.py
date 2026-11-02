#brute-force
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 1
        if n==1:
            return 1
        return self.climbStairs(n-1)+self.climbStairs(n-2)
#optimal
class Solution(object):
    def h(self,n:int,mp:dict[int,int])->int:
        if n==0 or n==1:
            return 1
        if n not in mp:
            mp[n]=self.h(n-1,mp)+ self.h(n-2,mp)
        return mp[n]
    def climbStairs(self, n):
        mp={}
        return self.h(n,mp)