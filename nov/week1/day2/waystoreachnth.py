#bruteforce
class Solution:
    def countWays(self, n: int) -> int:
        # code here
        if n<=2:
            return n
        return self.countWays(n-1)+self.countWays(n-2)
#optimal
class Solution:
    def countWays(self, n: int) -> int:
        # code here
        if n<=2:
            return n
        a,b=1,2
        for i in range(3,n+1):
            a,b=b,a+b
        return b