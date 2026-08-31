# Leetcode 4009: Minimum Possible Maximum Waiting Time
# https://leetcode.com/problems/minimum-possible-maximum-waiting-time/
# Solved on 31st of August, 2026
class Solution:
    def minMaxWaitingTime(self, demand: list[int], fuel: list[int]) -> int:
        """
        Calculates the minimum possible value of the maximum waiting time among all served cars to maximize the number of served cars.

        Args:
            demand (List[int]): The fuel demand for each car in sequence.
            fuel (List[int]): The initial fuel available in the two dispensers.

        Returns:
            int: The optimal minimum maximum waiting time, or -1 if no car can be served.
        """
        memo = {}

        def dfs(idx: int, f0: int, f1: int, w0: int, w1: int) -> tuple:

            if idx == len(demand):
                return (0, 0)

            if f0 < demand[idx] and f1 < demand[idx]:
                return (0, 0)

            state = (idx << 22) | (f0 << 16) | (f1 << 10) | (w0 << 5) | w1

            if state in memo:
                return memo[state]

            bestServed = -1
            bestNegWait = 1

            if f0 >= demand[idx]:
                waitTime = w0
                newW0 = demand[idx]
                newW1 = w1 - waitTime if w1 > waitTime else 0

                nextServed, negNextWait = dfs(idx + 1, f0 - demand[idx], f1, newW0, newW1)
                maxWait = waitTime if waitTime > -negNextWait else -negNextWait

                candServed = 1 + nextServed
                candNegWait = -maxWait

                if candServed > bestServed or (candServed == bestServed and candNegWait > bestNegWait):
                    bestServed = candServed
                    bestNegWait = candNegWait

            if f1 >= demand[idx]:
                waitTime = w1
                newW1 = demand[idx]
                newW0 = w0 - waitTime if w0 > waitTime else 0

                nextServed, negNextWait = dfs(idx + 1, f0, f1 - demand[idx], newW0, newW1)
                maxWait = waitTime if waitTime > -negNextWait else -negNextWait

                candServed = 1 + nextServed
                candNegWait = -maxWait

                if candServed > bestServed or (candServed == bestServed and candNegWait > bestNegWait):
                    bestServed = candServed
                    bestNegWait = candNegWait

            memo[state] = (bestServed, bestNegWait)

            return memo[state]

        ansServed, ansNegWait = dfs(0, fuel[0], fuel[1], 0, 0)

        return -ansNegWait if ansServed != 0 else -1