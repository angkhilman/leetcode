class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1, 2]
        if n > 2:
            for i in range(2, n):
                arr.append(arr[-1] + arr[-2])
        return arr[n-1]
