# Leetcode 3605: Minimum Stability Factor of Array
# https://leetcode.com/problems/minimum-stability-factor-of-array/
# Solved on 7th of December, 2025
import math


class Solution:
    def minStable(self, nums: list[int], maxC: int) -> int:
        """
        Calculates the minimum stability factor of the array.

        Args:
            nums: A list of integers representing the input array.
            maxC: An integer representing the maximum allowed operations.

        Returns:
            An integer representing the minimum stability factor.
        """
        n = len(nums)

        maxLog = n.bit_length()
        st = [nums]

        for k in range(1, maxLog):
            prev = st[-1]
            offset = 1 << (k - 1)
            current = [math.gcd(a, b) for a, b in zip(prev, prev[offset:])]
            st.append(current)

        def canAchieve(k):
            windowSize = k + 1
            if windowSize > n:
                return True

            logVal = windowSize.bit_length() - 1
            row = st[logVal]
            rightShift = windowSize - (1 << logVal)

            ops = 0
            i = 0
            limit = n - windowSize

            while i <= limit:
                rangeGcd = math.gcd(row[i], row[i + rightShift])

                if rangeGcd >= 2:
                    ops += 1
                    if ops > maxC:
                        return False
                    i += windowSize
                else:
                    i += 1
            return True

        # Binary search for the minimum stability factor
        low = 0
        high = n
        ans = n

        while low <= high:
            mid = (low + high) // 2
            if canAchieve(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans