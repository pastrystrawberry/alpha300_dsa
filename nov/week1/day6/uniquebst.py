class Solution:
    def numTrees(self, n: int) -> int:
        numtre=[1]*(n+1)
        for nodes in range(2,n+1):
            total =0
            for root in range(1,nodes+1):
                left=root-1
                right=nodes-root
                total+=numtre[left]*numtre[right]
            numtre[nodes]=total
        return numtre[n]