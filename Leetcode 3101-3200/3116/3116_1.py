# Leetcode 3116: Kth Smallest Amount With Single Denomination Combination
# https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/
# Solved on 21st of July, 2025
import math


class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        """
        Finds the k-th smallest amount that can be formed by combinations of given denominations.
        :param coins: A list of integers representing the available denominations.
        :param k: An integer representing the k-th smallest amount to find.
        :return: An integer representing the k-th smallest amount.
        """
        numCoins = len(coins)

        def countMultiples(value: int) -> int:
            count = 0
            # Iterate through all 2^n - 1 non-empty subsets using a bitmask
            for subsetMask in range(1, 1 << numCoins):
                currentLcm = 1
                subsetSize = 0
                for coinIndex in range(numCoins):
                    # Check if the coin is in the current subset
                    if (subsetMask >> coinIndex) & 1:
                        subsetSize += 1
                        currentLcm = (currentLcm * coins[coinIndex]) // math.gcd(currentLcm, coins[coinIndex])

                        if currentLcm > value:
                            currentLcm = value + 1
                            break

                if currentLcm <= value:
                    if subsetSize % 2 == 1:
                        count += value // currentLcm
                    else:
                        count -= value // currentLcm
            return count

        # Binary search fpr the k-th smallest amount
        low = 1
        high = min(coins) * k
        result = high

        while low < high:
            mid = low + (high - low) // 2

            achievableCount = countMultiples(mid)

            if achievableCount >= k:
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result