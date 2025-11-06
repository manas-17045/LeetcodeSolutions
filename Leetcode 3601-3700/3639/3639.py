# Leetcode 3639: Minimum Time to Activate String
# https://leetcode.com/problems/minimum-time-to-activate-string/
# Solved on 6th of November, 2025
class Solution:
    def minTime(self, s: str, order: list[int], k: int) -> int:
        """
        Calculates the minimum time required to activate at least k valid substrings.
        :param s: The input string.
        :param order: A list representing the order in which characters are activated.
        :param k: The minimum number of valid substrings required.
        :return: The minimum time (index in order) to achieve k valid substrings, or -1 if not possible.
        """
        n = len(s)
        totalSubstrings = n * (n + 1) // 2

        if k > totalSubstrings:
            return -1

        def check(t):
            isNewA = [False] * n

            for i in range(t + 1):
                isNewA[order[i]] = True

            invalidCount = 0
            currentLength = 0

            for i in range(n):
                if isNewA[i]:
                    invalidCount += currentLength * (currentLength + 1) // 2
                    currentLength = 0
                else:
                    currentLength += 1

            invalidCount += currentLength * (currentLength + 1) // 2

            validCount = totalSubstrings - invalidCount
            return validCount >= k

        ans = -1
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans