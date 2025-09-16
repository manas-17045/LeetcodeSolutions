# Leetcode 2522: Partition String Into Substrings With Values at Most K
# https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/
# Solved on 16th of September, 2025
class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        """
        Partitions a string `s` into the minimum number of substrings such that the numerical value
        of each substring is at most `k`.

        Args:
            s (str): The input string consisting of digits.
            k (int): The maximum allowed value for each substring.
        Returns:
            int: The minimum number of partitions, or -1 if it's impossible to partition.
        """
        numPartitions = 1
        currentVal = 0

        for digitChar in s:
            digitVal = int(digitChar)

            if digitVal > k:
                return -1

            potentialVal = currentVal * 10 + digitVal

            if potentialVal <= k:
                currentVal = potentialVal
            else:
                numPartitions += 1
                currentVal = digitVal

        return numPartitions