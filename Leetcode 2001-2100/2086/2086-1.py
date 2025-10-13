# Leetcode 2086: Minimum Number of Food Buckets to Feed the Hamsters
# https://leetcode.com/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/
# Solved on 11th of October, 2025
class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        """
        Calculates the minimum number of food buckets required to feed all hamsters.

        Args:
            hamsters (str): A string representing the arrangement of hamsters and empty spaces.
                            'H' denotes a hamster, '.' denotes an empty space.
        Returns:
            int: The minimum number of food buckets needed. Returns -1 if it's impossible to feed all hamsters.
        """
        hamstersList = list(hamsters)
        n = len(hamstersList)
        bucketsCount = 0

        for i in range(n):
            if hamstersList[i] == 'H':
                if i > 0 and hamstersList[i - 1] == 'B':
                    continue

                if i + 1 < n and hamstersList[i + 1] == '.':
                    hamstersList[i + 1] = 'B'
                    bucketsCount += 1
                elif i > 0 and hamstersList[i - 1] == '.':
                    hamstersList[i - 1] = 'B'
                    bucketsCount += 1
                else:
                    return -1

        return bucketsCount