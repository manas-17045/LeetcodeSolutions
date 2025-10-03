# Leetcode 3524: Find X Value of Array I
# https://leetcode.com/problems/find-x-value-of-array-i/
# Solved on 3rd of October, 2025
class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        """
        Calculates the number of non-empty subarrays whose product modulo k equals a specific residue.

        Args:
            nums: A list of integers.
            k: An integer representing the modulo.
        Returns:
            A list where the element at index `x` is the count of subarrays whose product % k == x.
        """
        # result[x] = number of non-empty subarrays whose product % k == x
        res = [0] * k
        if not nums:
            return res

        # curr[r] = number of subarrays ending at previous index with residue r
        curr = [0] * k

        for val in nums:
            x = val % k
            new = [0] * k

            # Extend previous subarrays by multiplying current element
            for r in range(k):
                cnt = curr[r]
                if cnt:
                    new[(r * x) % k] += cnt

            # Start a new subarray consisting of only this element
            new[x] += 1

            # Accumulate into result
            for r in range(k):
                if new[r]:
                    res[r] += new[r]

            # Move window of "ending at previous index" forward
            curr = new

        return res