class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def h(left,right):
            if left>right:
                return 
            s[left],s[right]=s[right],s[left]
            return h(left+1,right-1)
        

        return h(0,len(s)-1)