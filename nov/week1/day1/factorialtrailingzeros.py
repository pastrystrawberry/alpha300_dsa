#brute-force
class Solution:
    def trailingZeroes(self, n: int) -> int:
        f = 1
        for i in range(1, n+1):
            f*= i
        count = 0
        while f> 0 and f% 10== 0:
            count+=1
            fact//= 10
        return count
#optimal
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count=0
        while n>0:
            n //=5
            count+=n
        return count