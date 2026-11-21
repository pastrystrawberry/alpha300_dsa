
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l=0
        r=len(nums)-1
        ans=[0]*len(nums)
        k=len(nums)-1
        while l<=r:
            if abs(nums[l])>abs(nums[r]):
                ans[k]=nums[l]*nums[l]
                l+=1
            else:
                ans[k]=nums[r]*nums[r]
                r-=1
            k-=1
        return ans
