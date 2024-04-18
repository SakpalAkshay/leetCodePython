class Solution:
    def sumZero(self, n: int) -> List[int]:
        m = n // 2
        out = []
        for i in range(1,m+1):
            out.append(i)
            out.append(-i)
        
        if n % 2==1:
            out.append(0)
        return out

