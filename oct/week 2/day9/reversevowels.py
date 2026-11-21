
class Solution:
    def reverseVowels(self, s: str) -> str:
        arr=list(s)
        vowels="aeiouAEIOU"
        l=0
        r=len(arr)-1
        while l<r:
            if arr[l] not in vowels:
                l+=1
            elif arr[r] not in vowels:
                r-=1
            else:
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1
        return "".join(arr)
