# Leetcode 3449: Maximize the Minimum Game Score
# https://leetcode.com/problems/maximize-the-minimum-game-score/
# Solved on 15th of December, 2025
class Solution:
    def maxScore(self, points: list[int], m: int) -> int:
        """
        Maximizes the minimum game score achievable given a list of points and a maximum number of moves.

        Args:
            points: A list of integers representing the points at each position.
            m: An integer representing the maximum number of moves allowed.
        Returns:
            An integer representing the maximum possible minimum game score.
        """
        n = len(points)

        def check(target):
            if target == 0:
                return True

            moves = 1
            currentVisits = 1

            for i in range(n - 1):
                if moves > m:
                    return False

                pVal = points[i]
                required = (target + pVal - 1) // pVal

                extra = 0
                if required > currentVisits:
                    extra = required - currentVisits

                moves += 2 * extra

                nextVisits = extra

                if i == n - 2:
                    pLast = points[n - 1]
                    requiredLast = (target + pLast - 1) // pLast
                    if nextVisits >= requiredLast:
                        return moves <= m

                moves += 1
                currentVisits = nextVisits + 1

            if moves > m:
                return False

            pLast = points[n - 1]
            requiredLast = (target + pLast - 1) // pLast

            extraLast = 0
            if requiredLast > currentVisits:
                extraLast = requiredLast - currentVisits

            moves += 2 * extraLast
            return moves <= m

        left, right = 0, 2 * 10 ** 15
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans