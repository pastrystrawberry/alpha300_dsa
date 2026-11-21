
def maxSum(nums,k):
    total=sum(nums[:k])
    best=total
    for i in range(k,len(nums)):
        total+=nums[i]
        total-=nums[i-k]
        best=max(best,total)
    return best

nums=[2,1,5,1,3,2]
k=3
print(maxSum(nums,k))
