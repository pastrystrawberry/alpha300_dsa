class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mp={}
        res=[]
        for i,a in enumerate(nums):
            if nums[i] in mp:
                mp[nums[i]]+=1
            else:
                mp[nums[i]]=1
            if mp[nums[i]]==2:
                res.append(nums[i])
        return res

