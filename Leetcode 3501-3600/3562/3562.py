# Leetcode 3562: Maximum Profit from Trading Stocks with Discounts
# https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/
# Solved on 28th of November, 2025
class Solution:
    def maxProfit(self, n: int, present: list[int], future: list[int], hierarchy: list[list[int]], budget: int) -> int:
        """
        Calculates the maximum profit from trading stocks with discounts.

        Args:
            n (int): The number of stocks.
            present (list[int]): A list of present prices for each stock.
            future (list[int]): A list of future prices for each stock.
            hierarchy (list[list[int]]): A list of parent-child relationships representing the stock hierarchy.
            budget (int): The maximum budget available for trading.

        Returns:
            int: The maximum profit achievable.
        """

        adj = [[] for _ in range(n + 1)]
        for u, v in hierarchy:
            adj[u].append(v)

        def dfs(u):
            dpBuy = [-float('inf')] * (budget + 1)
            dpSkip = [-float('inf')] * (budget + 1)
            dpBuy[0] = 0
            dpSkip[0] = 0

            for v in adj[u]:
                childResBuy, childResSkip = dfs(v)

                nextBuy = [-float('inf')] * (budget + 1)
                states1 = [(c, p) for c, p in enumerate(dpBuy) if p != -float('inf')]
                states2 = [(c, p) for c, p in enumerate(childResBuy) if p != -float('inf')]
                for c1, p1 in states1:
                    for c2, p2 in states2:
                        if c1 + c2 <= budget:
                            if p1 + p2 > nextBuy[c1 + c2]:
                                nextBuy[c1 + c2] = p1 + p2
                dpBuy = nextBuy

                nextSkip = [-float('inf')] * (budget + 1)
                states1 = [(c, p) for c, p in enumerate(dpSkip) if p != -float('inf')]
                states2 = [(c, p) for c, p in enumerate(childResSkip) if p != -float('inf')]
                for c1, p1 in states1:
                    for c2, p2 in states2:
                        if c1 + c2 <= budget:
                            if p1 + p2 > nextSkip[c1 + c2]:
                                nextSkip[c1 + c2] = p1 + p2
                dpSkip = nextSkip

            resParentBuy = list(dpSkip)
            costDiscount = present[u - 1] // 2
            profDiscount = future[u - 1] - costDiscount

            if costDiscount <= budget:
                for c, p in enumerate(dpBuy):
                    if p != -float('inf') and c + costDiscount <= budget:
                        if p + profDiscount > resParentBuy[c + costDiscount]:
                            resParentBuy[c + costDiscount] = p + profDiscount

            resParentSkip = list(dpSkip)
            costFull = present[u - 1]
            profFull = future[u - 1] - costFull

            if costFull <= budget:
                for c, p in enumerate(dpBuy):
                    if p != -float('inf') and c + costFull <= budget:
                        if p + profFull > resParentSkip[c + costFull]:
                            resParentSkip[c + costFull] = p + profFull

            return resParentBuy, resParentSkip

        _, rootRes = dfs(1)
        return int(max(rootRes))