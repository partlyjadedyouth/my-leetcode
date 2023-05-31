class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sums = [sum(account) for account in accounts]
        return max(sums)
