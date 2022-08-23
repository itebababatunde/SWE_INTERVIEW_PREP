class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        num = abs(n)
        steps = 0
        
        while num >1 :
            num = num/4  
            steps+=1
        return True if 4**steps == n else False
        