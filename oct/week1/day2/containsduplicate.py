class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x={}
        for i in nums:
            if i in x:
                return True
            x[i]=1
        return False
