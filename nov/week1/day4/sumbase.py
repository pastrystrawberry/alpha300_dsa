class Solution:
    def sumBase(self, n: int, k: int) -> int:
        total =0
        while n>0:
            rem=n%k
            total+=rem
            n=n//k
        return total
        