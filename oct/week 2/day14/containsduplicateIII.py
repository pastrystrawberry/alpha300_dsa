
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff<0:
            return False

        buckets={}
        size=valueDiff+1

        for i in range(len(nums)):
            bucket=nums[i]//size

            if bucket in buckets:
                return True

            if bucket-1 in buckets and abs(nums[i]-buckets[bucket-1])<=valueDiff:
                return True

            if bucket+1 in buckets and abs(nums[i]-buckets[bucket+1])<=valueDiff:
                return True

            buckets[bucket]=nums[i]

            if i>=indexDiff:
                oldbucket=nums[i-indexDiff]//size
                del buckets[oldbucket]

        return False
