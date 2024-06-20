class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Initialize the first two steps
        first, second = 1, 2
        
        # Calculate the ways to reach each step from 3 to n
        for _ in range(3, n + 1):
            first, second = second, first + second
        
        return second
