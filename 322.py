# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         arr = [amount + 1] * (amount + 1)
#         arr[0] = 0
#         print(arr)
#         for i in range(amount + 1):
#             for j in coins:
#                 if i - j == 0:
#                     arr[i] = 1
#         for i in range(amount + 1):
#             for j in coins:
#                 if i - j >= 0 and arr[i] != 1:
#                     arr[i] = min(arr[i], arr[i - j] + 1)
#         return arr[-1] if arr[-1] < amount + 1 else -1




class Solution:
    def __init__(self):
        self.memo={}
    
    def recCoin(self, coins, amount):
        if amount in self.memo:
            return self.memo[amount]
        if amount == 0:
            return 0
        if amount < 0:
            return 10**15
        if amount in coins:
            return 1
        min_c = 10**15
        for i in coins:
            min_c = min(min_c, self.recCoin(coins, amount - i) + 1)
            self.memo[amount] = min_c
        return self.memo[amount]
        
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans = self.recCoin(coins, amount)
        return -1 if ans == 10**15 else ans
        #F(n) = min(F(n-c)) + 1
        #f(c) = 1
        #f(-inf, 0) = inf

        
        
