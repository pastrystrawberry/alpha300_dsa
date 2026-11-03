class Solution:
    def canJump(self, nums: list[int]) -> bool:
        maxr=0
        for i in range(len(nums)):
            if i>maxr:
                return False
            maxr=max(maxr,i+nums[i])
        return True