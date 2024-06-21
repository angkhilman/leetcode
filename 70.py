class Solution:
    def __init__(self):
        self.memo = {}
    def rec(self, n):
        if n in self.memo:
            return self.memo[n]
        if n == 1:
            return 1
        if n == 2:
            return 2
        self.memo[n] = self.rec(n - 1) + self.rec(n - 2)
        return self.memo[n]

    def climbStairs(self, n: int) -> int:
        return self.rec(n)
