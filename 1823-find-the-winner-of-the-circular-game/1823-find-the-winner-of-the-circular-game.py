class Solution:
    def josephus(self,n,k):
        if n == 1:
            return 0
        return (self.josephus(n-1,k)+k)%n
    def findTheWinner(self,n,k):
        return self.josephus(n,k)+1