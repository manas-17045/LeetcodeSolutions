# Leetcode 2086: Minimum Number of Food Buckets to Feed the Hamsters
# https://leetcode.com/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/
# Solved on 11th of October, 2025
class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        """
        Calculates the minimum number of buckets needed to feed all hamsters.
        :param hamsters: A string representing the hamsters' arrangement, where 'H' is a hamster and '.' is an empty space.
        :return: The minimum number of buckets required, or -1 if it's impossible to feed all hamsters.
        """
        s = list(hamsters)
        buckets = 0

        for i in range(len(s)):
            if s[i] == 'H':
                # Check if hamster is already fed by adjacent bucket
                if (i - 1 >= 0 and s[i - 1] == 'B') or (i + 1 < len(s) and s[i + 1] == 'B'):
                    continue

                # Try to place bucket at i + 1 first (greedy approach)
                if i + 1 < len(s) and s[i + 1] == '.':
                    s[i + 1] = 'B'
                    buckets += 1
                # Otherwise, try i - 1
                elif i - 1 >= 0 and s[i - 1] == '.':
                    s[i - 1] = 'B'
                    buckets += 1
                # Can't feed this hamster
                else:
                    return -1

        return buckets