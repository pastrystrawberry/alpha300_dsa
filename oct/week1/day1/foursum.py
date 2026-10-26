class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums=sorted(nums)
        res,q=[],[]
        def ks(k,start,target):
            if k!=2:
                for i in range(start,len(nums)-k+1):
                    if i>start and nums[i]==nums[i-1]:
                        continue
                    q.append(nums[i])
                    ks(k-1,i+1,target-nums[i])
                    q.pop()
                return
            l,r=start,len(nums)-1
            while(l<r):
                if nums[l]+nums[r]<target:
                    l=l+1
                elif nums[l]+nums[r]>target:
                    r=r-1
                else:
                    res.append(q+[nums[l],nums[r]])
                    l=l+1
                    r=r-1
                    while l<r and nums[l]==nums[l-1]:
                        l=l+1
        ks(4,0,target)
        return res