# Leetcode 3251: Find the Count of Monotonic Pairs II
# https://leetcode.com/problems/find-the-count-of-monotonic-pairs-ii/
# Solved on 3rd of June, 2025

class Solution:
    def countOfPairs(self, nums: list[int]) -> int:
        """
        Finds the number of pairs of arrays (arr1, arr2) such that:
        1. arr1 and arr2 have the same length as nums.
        2. 0 <= arr1[i] <= nums[i] for all i.
        3. 0 <= arr2[i] <= nums[i] for all i.
        4. arr1 is non-decreasing (arr1[i] <= arr1[i+1] for all i).
        5. arr2 is non-increasing (arr2[i] >= arr2[i+1] for all i).
        6. arr1[i] + arr2[i] = nums[i] for all i.

        This problem can be reduced to finding the number of non-decreasing arrays arr1
        such that 0 <= arr1[i] <= nums[i] and arr1[i] - arr1[i-1] >= nums[i] - nums[i-1].
        This is because arr2[i] = nums[i] - arr1[i], and the non-increasing condition
        for arr2 translates to nums[i] - arr1[i] >= nums[i+1] - arr1[i+1], which simplifies
        to arr1[i+1] - arr1[i] >= nums[i+1] - nums[i].

        Args:
            nums: A list of integers.
        """
        n = len(nums)
        mod = 10**9 + 7

        # Maximum possible value for any arr1[i], based on nums[i] <= 1000
        maxArrOneValAllowed = 1000

        # prevDp[val] stores dp[i - 1][val]
        prevDp = [0] * (maxArrOneValAllowed + 1)

        # Base case for i = 0 (arr1[0])
        # arr1[0] can be any value 'val' from 0 to nums[0]
        # For each such val, there's 1 way.
        for valForArrOneAtIndexZero in range(nums[0] + 1):
            # Condition valForArrOneAtIndexZero <= maxxArrOneValAllowed is always true
            # since nums[0] <= 1000.
            prevDp[valForArrOneAtIndexZero] = 1

        # Iterate for i from 1 to (n - 1) (representing ass1[i] up yo arr1[n - 1])
        for i in range(1, n):
            # currentDp[val] stores dp[i][val]
            currentDp = [0] * (maxArrOneValAllowed + 1)

            # Calculate prefix sums of prevDp (dp[i - 1])
            prefixSumOfPrevDp = [0] * (maxArrOneValAllowed + 1)
            runningSum = 0
            for k in range(maxArrOneValAllowed + 1):
                runningSum = (runningSum + prevDp[k]) % mod
                prefixSumOfPrevDp[k] = runningSum

            # Determine the limit for currentArr1Val
            limitForCurrentArrOneVal = nums[i]

            # Iterate over possible values for arr1[i]
            for currentArrOneVal in range(limitForCurrentArrOneVal + 1):
                # Determine the upper bound for prevArr1Val
                upperBoundForPrevArrOneVal = currentArrOneVal

                deltaNums = nums[i] - nums[i - 1]
                upperBoundForPrevArrOneVal = min(upperBoundForPrevArrOneVal, (currentArrOneVal - deltaNums))

                # If the calculated upper bound is negative, no valid prevArr1Val exists
                if upperBoundForPrevArrOneVal < 0:
                    currentDp[currentArrOneVal] = 0
                else:
                    # The sum dp[i-1][0] + ... + dp[i-1][upperBoundForPrevArrOneVal]
                    # is prefixSumOfPrevDp[upperBoundForPrevArrOneVal].
                    currentDp[currentArrOneVal] = prefixSumOfPrevDp[upperBoundForPrevArrOneVal]

            # Current row becomes previous row for the next iteration
            prevDp = currentDp

        # The final answer is the sum of all dp[n - 1][val].
        totalCount = 0
        for countForVal in prevDp:
            # prevDp now holds dp[n - 1] values.
            totalCount = (totalCount + countForVal) % mod

        return totalCount