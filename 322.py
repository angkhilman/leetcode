class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [amount + 1] * (amount + 1)
        arr[0] = 0
        print(arr)
        for i in range(amount + 1):
            for j in coins:
                if i - j == 0:
                    arr[i] = 1
        for i in range(amount + 1):
            for j in coins:
                if i - j >= 0 and arr[i] != 1:
                    arr[i] = min(arr[i], arr[i - j] + 1)
        return arr[-1] if arr[-1] < amount + 1 else -1
        
