# Leetcode 2522: Partition String Into Substrings With Values at Most K
# https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/
# Solved on 16th of September, 2025
class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        """
        Partitions a string `s` into the minimum number of substrings such that each substring's integer value is less than or equal to `k`.

        :param s: The input string consisting of digits.
        :param k: The maximum allowed integer value for each substring.
        :return: The minimum number of partitions, or -1 if it's impossible to partition.
        """
        # If any single digit is greater tha k, impossible
        if any(int(ch) > k for ch in s):
            return -1

        count = 1
        curr = int(s[0])

        for ch in s[1:]:
            d = int(ch)
            # Try to append digit to current number
            if curr * 10 + d <= k:
                curr = curr * 10 + d
            else:
                # Start a new substring with this digit
                count += 1
                curr = d

        return count