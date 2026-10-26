class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums=sorted(nums)
        res=[]
        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while(l<r):
                ts=a+nums[l]+nums[r]
                if(ts<0):
                    l=l+1
                elif ts>0:
                    r=r-1
                else:
                    res.append([a,nums[l],nums[r]])
                    l=l+1
                    r=r-1
                    while l<r and nums[l]==nums[l-1]:
                        l=l+1
        return res