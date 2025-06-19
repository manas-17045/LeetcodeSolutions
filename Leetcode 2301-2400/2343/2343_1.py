# Leetcode 2343: Query Kth Smallest Trimmed Number
# https://leetcode.com/problems/query-kth-smallest-trimmed-number/
# Solved on 18th of June, 2025

class Solution:
    def smallestTrimmedNumber(self, nums: list[str], queries: list[list[str]]) -> list[int]:
        """
        Given a 0-indexed array of strings nums, where each string represents a positive integer
        with the same length, and a 0-indexed array of queries, where each query[i] is a pair
        of integers [ki, trimi], return an array answer, where answer[i] is the index of the
        ki-th smallest number after trimming each number in nums to its rightmost trimi digits.

        Args:
            nums (list[str]): A list of strings, each representing a positive integer.
            queries (list[list[str]]): A list of queries, where each query is [k, trim].
                                       k is the 1-based index of the smallest number to find.
                                       trim is the number of rightmost digits to consider.

        Returns:
            list[int]: A list of integers, where each element is the original index of the
                       k-th smallest trimmed number for the corresponding query.
        """
        ans = []
        # Cache to store sorted (value, index) pairs for each trim object
        cache = {}

        for k, trim in queries:
            # Check if the results for this trim length are already cached
            if trim not in cache:
                # If not cached, compute and sort the pairs
                pairs = []
                for idx, numStr in enumerate(nums):
                    # Get the rightmost 'trim' digits
                    trimmedStr = numStr[-trim:]
                    # Convert the trimmed string to an integer
                    val = int(trimmedStr)
                    # Store the numeric value and original index as a pair
                    pairs.append((val, idx))

                # Sort the pairs in ascending order
                pairs.sort()

                # Store the sorted pairs in the cache for future use
                cache[trim] = pairs

            # Retrieve the sorted list for the current trim length from the cache
            sortedPairs = cache[trim]

            # Append the original index (the second element of the pair) to the answer list
            ans.append(sortedPairs[k - 1][1])

        return ans