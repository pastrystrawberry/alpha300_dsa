class Solution:
    def validSquare(self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:
        if p1==p2==p3==p4:return False
        def d(x,y):
            return(x[0]-y[0])**2+(x[1]-y[1])**2
        ls=[d(p1,p2),d(p1,p3),d(p1,p4),d(p2,p3),d(p2,p4),d(p3,p4)]
        ls.sort()
        if ls[0]==ls[1]==ls[2]==ls[3]:
            if ls[4]==ls[5]:
                return True
        return False

        