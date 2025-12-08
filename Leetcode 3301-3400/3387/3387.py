# Leetcode 3387: Maximize Amount After Two Days of Conversions
# https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/
# Solved on 8th of December, 2025
from collections import defaultdict, deque


class Solutions:
    def maxAmount(self, initialCurrency: str, pairs1: list[list[str]], rates1: list[float], pairs2: list[list[str]], rates2: list[float]) -> float:
        """
        Calculates the maximum amount of initial currency after two days of conversions.

        Args:
            initialCurrency (str): The starting currency.
            pairs1 (list[list[str]]): A list of currency pairs for day 1 conversions.
            rates1 (list[float]): A list of conversion rates corresponding to pairs1.
            pairs2 (list[list[str]]): A list of currency pairs for day 2 conversions.
            rates2 (list[float]): A list of conversion rates corresponding to pairs2.

        Returns:
            float: The maximum amount of initial currency after two days of conversions.
        """
        def getRates(pairs, rates):
            adj = defaultdict(list)
            for (u, v), r in zip(pairs, rates):
                adj[u].append((v, r))
                adj[v].append((u, 1.0 / r))

            ratesMap = {}
            queue = deque([(initialCurrency, 1.0)])
            ratesMap[initialCurrency] = 1.0

            while queue:
                curr, val = queue.popleft()
                for nxt, r in adj[curr]:
                    if nxt not in ratesMap:
                        newVal = val * r
                        ratesMap[nxt] = newVal
                        queue.append((nxt, newVal))
            return ratesMap

        day1Rates = getRates(pairs1, rates1)
        day2Rates = getRates(pairs2, rates2)

        maxVal = 0.0
        for currency, val1 in day1Rates.items():
            if currency in day2Rates:
                val2 = day2Rates[currency]
                maxVal = max(maxVal, val1 / val2)

        return maxVal