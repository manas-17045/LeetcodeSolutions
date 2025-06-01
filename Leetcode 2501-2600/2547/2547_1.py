# Leetcode 2547: Minimum Cost to Split an Array
# https://leetcode.com/problems/minimum-cost-to-split-an-array/
# Solved on 1st of June, 2025
import math


class Solution:
    def minCost(self, nums: list[int], k: int) -> int:
        """
        Calculates the minimum cost to split an array `nums` into several subarrays.

        The cost of splitting an array is the sum of the costs of each subarray.
        The cost of a subarray is defined as `k + trimmed_length`, where `trimmed_length`
        is the number of elements that need to be removed so that all remaining elements
        in the subarray are unique.

        This is a dynamic programming problem. `dp[i]` stores the minimum cost to split
        the prefix `nums[0...i-1]`. To calculate `dp[i]`, we consider all possible
        last subarrays ending at index `i-1`. If the last subarray starts at index `j`,
        the cost is `dp[j] + importance(nums[j...i-1])`. We take the minimum over all
        possible `j` from 0 to `i-1`.

        The importance of a subarray is `k + trimmed_length` of that subarray.
        """
        # Get the length of the input array of nums.
        n = len(nums)
        # dp[i] will store the minimum cost to split the prefix nums[0...(i - 1)].
        # Initialize dp array with infinity, as we are looking for minimum costs.
        dp = [math.inf] * (n + 1)
        # Base case: The cost to split an empty prefix (nums[0...-1]) is 0.
        dp[0] = 0

        # Iterate through all possible end positions 'i' for the current segment of the array.
        # 'i' represents the length of the prefix nums[0...(i - 1)] being considered.
        for i in range(1, n + 1):
            # For each prefix nums[0...(i - 1)], we calculate sp[i].
            # Frequency map for elements in the current subarray nums[j_idx...(i - 1)].
            currentSubarrayCounts: dict[int, int] = {}
            # Trimmed length of the current subarray nums[j_idx...(i - 1)].
            currentSubarrayTrimmedLength = 0

            # Iterate backwards from 'i - 1' down to 0 for the start index 'j_idx' of the last subarray.
            # The last subarray considered is nums[j_idx...(i - 1)]. This subarray is built by adding nums[j_idx] to its left end at each step of this inner loop.
            for j_idx in range(i - 1, -1, -1):
                # Get the element at nums[j_idx].
                elementBeingAdded = nums[j_idx]

                # Update the frequency count of elementBeingAdded in currentSubarrayCounts.
                # Get its previous count in nums[(j_idx + 1)...(i - 1)].
                oldCountOfElement = currentSubarrayCounts.get(elementBeingAdded, 0)
                # Increment its count for nums[j_idx...(i - 1)].
                currentSubarrayCounts[elementBeingAdded] = oldCountOfElement + 1
                # Store the new count
                newCountOfElement = oldCountOfElement + 1

                # Update currentSubarrayTrimmedLength based on the new count of elementBeingAdded.
                if newCountOfElement == 2:
                    # If count becomes 2, this element (and its previous occurrence) now contributes to trimmmedLength. Total contribution is 2.
                    currentSubarrayTrimmedLength += 2
                elif newCountOfElement > 2:
                    # If count is > 2, this element was already contributing (its previous occurrences were counted); this new occurrence adds 1 more to trimmed_length.
                    currentSubarrayTrimmedLength += 1

                # If newCountOfElement == 1 (i.e., oldCountOfElement == 0), it's unique in the current subarray and doesn't add to trimmedLength.
                # Calculate the importance value of he current subarray nums[j_idx...(i - 1)].
                importance = k + currentSubarrayTrimmedLength

                # If dp[j_idx] (cost for prefix nums[0...(j_idx - 1)]) is reachable (not infinity).
                if dp[j_idx] != math.inf:
                    # Update dp[i] with the minimum cost found so far.
                    # This is the cost of splitting nums[0...(j_idx - 1)] (which is dp[j_idx]) plus the importance of the last subarray nums[j_idx...(i - 1)].
                    dp[i] = min(dp[i], dp[j_idx] + importance)

        # The final answer is sp[n], representing the minimum cost to split the entire array nums[0...(n - 1)].
        return dp[n]
