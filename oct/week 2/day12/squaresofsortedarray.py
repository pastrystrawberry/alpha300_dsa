
class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        n=len(nums)
        left=-1
        right=-2
        maxval=nums[0]
        minval=nums[-1]

        for i in range(1,n):
            maxval=max(maxval,nums[i])
            if nums[i]<maxval:
                right=i

        for i in range(n-2,-1,-1):
            minval=min(minval,nums[i])
            if nums[i]>minval:
                left=i

        return right-left+1
