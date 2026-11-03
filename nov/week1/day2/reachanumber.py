class Solution:
    def reachNumber(self, target: int) -> int:
        if target==0:
            return 0
        target =abs(target)
        s =0 
        step =0
        while(s<target):
            s+=step
            step=step+1
        while((target-s)%2!=0):
            s+=step
            step=step+1
        return step-1
            