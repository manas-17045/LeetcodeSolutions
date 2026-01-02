# Leetcode 3332: Maximum Points Tourist Can Earn
# https://leetcode.com/problems/maximum-points-tourist-can-earn/
# Solved on 2nd of January, 2026
class Solution:
    def maxScore(self, n: int, k: int, stayScore: list[list[int]], travelScore: list[list[int]]) -> int:
        """
        Calculates the maximum score a tourist can earn over k days.

        Args:
            n (int): The number of cities.
            k (int): The number of days.
            stayScore (list[list[int]]): A 2D list where stayScore[i][j] is the score earned for staying in city j on day i.
            travelScore (list[list[int]]): A 2D list where travelScore[i][j] is the score earned for traveling from city i to city j.

        Returns:
            int: The maximum score the tourist can earn.
        """
        dp = [0] * n

        for i in range(k):
            currentStayScore = stayScore[i]
            nextDp = [0] * n

            for j in range(n):
                nextDp[j] = dp[j] + currentStayScore[j]

            for prev in range(n):
                prevScore = dp[prev]
                travelRow = travelScore[prev]
                for curr in range(n):
                    score = prevScore + travelRow[curr]
                    if score > nextDp[curr]:
                        nextDp[curr] = score

            dp = nextDp

        return max(dp)