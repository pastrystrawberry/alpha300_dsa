class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mp={}
        for i,num in enumerate(nums):
            if num in mp and i-mp[num]<=k:
                return True
            mp[num]=i
        return False
            
        