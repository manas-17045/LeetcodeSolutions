# Leetcode 1534: Count Good Triplets
# https://leetcode.com/problems/count-good-triplets/

class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        """
        Calculates the number of "good triplets" in the array. A triplet (i, j, k) in the array is considered
        a "good triplet" if the following conditions are met:
        - `0 <= i < j < k < len(arr)`
        - `abs(arr[i] - arr[j]) <= a`
        - `abs(arr[j] - arr[k]) <= b`
        - `abs(arr[i] - arr[k]) <= c`

        This function checks all possible triplets in the array that satisfy the above constraints and
        returns the total count of such triplets.

        :param arr: The input array of integers to be analyzed.
        :param a: An integer determining the maximum absolute difference allowed between arr[i] and arr[j].
        :param b: An integer determining the maximum absolute difference allowed between arr[j] and arr[k].
        :param c: An integer determining the maximum absolute difference allowed between arr[i] and arr[k].
        :return: The total number of triplets in the array that meet the specified conditions, as an integer.
        """
        count = 0
        n = len(arr)

        # A triplet requires at least 3 elements in the array
        if n < 3:
            return 0

        # Iterate through all possible index combinations i, j, k such that 0 <= i < j < k, n.
        # The loop ranges ensure this ordering.
        for i in range(n - 2):  # i ranges from 0 to n - 3
            for j in range(i + 1, n - 1):  # j ranges from i + 1 to n - 2

                # Optimization: Check the first condition (involving i and j) early.
                # If abs(arr[i] - arr[j]) > `a`, then no triplet starting with this (i, j)
                # pair can be good, so we can skip the innermost loop for this j.
                if abs(arr[i] - arr[j]) <= a:

                    # Only if the first condition holds, iterate thriugh possible k value.
                    for k in range(j + 1, n):   # k ranges from j + 1 to n - 1
                        # Check the remaining two conditions involving j, k and i, k.
                        # Condition 2: abs(arr[j] - arr[k]) <= b
                        # Condition 3: abs(arr[i] - arr[k]) <= c
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            # If all three conditions are met, increment the count.
                            count += 1

        # Return the final count of good triplets.
        return count