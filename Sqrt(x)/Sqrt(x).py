class Solution:
    def mySqrt(self, x: int) -> int:
        
        odd = 1
        sub = x - odd
        i = 0
        while sub >= 0:
            i += 1
            odd += 2
            sub = sub - odd

        return i