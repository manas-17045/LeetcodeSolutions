# Leetcode 3355: Zero Array Transformation I
# https://leetcode.com/problems/zero-array-transformation-i/
# Solved on 20th of May, 2025

class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        """
        Determines if an array can be transformed into a zero array using a set of queries.

        Each query represents a range of indices [L, R] where the values within that range can be decremented.
        The function checks if it's possible to make all elements of the array zero by applying the queries.

        Args:
            nums (list[int]): The input array of integers.
            queries (list[list[int]]): A list of queries, where each query is a list [L, R] representing the start and end indices of a range.

        Returns:
            bool: True if the array can be transformed into a zero array, False otherwise.
        """
        n = len(nums)

        # delta[i] will store the net change in the count of covering queries
        # when moving from index i-1 to i.
        # An operation on range [L, R] adds 1 to the coverage for indices L through R.
        # This is modeled by adding 1 at delta[L] and subtracting 1 at delta[R+1].
        # The delta array needs to be of size n+1 because if R = n-1 (last index of nums),
        # then R+1 = n. delta[n] is a valid index in an array of size n+1.
        delta = [0] * (n + 1)

        for L, R in queries:
            delta[L] += 1
            # R is an index in nums, so R <= n-1.
            # Therefore, R+1 <= n.
            # delta[R+1] is always a valid index for an array of size n+1.
            delta[R + 1] -= 1

        # Calculate the actual number of queries covering each index i by taking prefix sums of delta.
        # current_coverage_count accumulates delta values. At index i of the loop,
        # it represents the total number of queries covering nums[i].
        current_coverage_count = 0
        for i in range(n):  # Iterate through indices 0 to (n - 1) of nums
            current_coverage_count += delta[i]

            # If the initial value nums[i] requires more decrements than
            # the number of queries covering this index (current_coverage_count),
            # then it's impossible to make nums[i] zero.
            if nums[i] > current_coverage_count:
                return False

        # If the loop completes, it means for every index i, nums[i] <= num_covering_queries[i].
        # Thus, it's possible to make the entire array zero.
        return True