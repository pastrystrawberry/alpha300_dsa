class Solution:
    def countPairs(self, arr, target): 
        mp={}
        count=0
        for i in range(len(arr)):
            needed=target-arr[i]
            if needed in mp:
                count+=mp[needed]
            if arr[i] in mp:
                mp[arr[i]]+=1
            else:
                mp[arr[i]]=1
        return count
                