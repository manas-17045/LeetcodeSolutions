# Leetcode 1482: Minimum Number of Days to Make m Bouquets
# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
# Solved on 11th of December, 2025
class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        """
        Calculates the minimum number of days required to make 'm' bouquets,
        where each bouquet requires 'k' adjacent flowers to be bloomed.

        Args:
            bloomDay (list[int]): A list where bloomDay[i] is the day on which the i-th flower will bloom.
            m (int): The number of bouquets to make.
            k (int): The number of adjacent flowers required for one bouquet.
        Returns:
            int: The minimum number of days to make 'm' bouquets, or -1 if it's impossible.
        """
        if m * k > len(bloomDay):
            return -1

        leftDay = min(bloomDay)
        rightDay = max(bloomDay)

        while leftDay < rightDay:
            midDay = (leftDay + rightDay) // 2
            bouquetsCount = 0
            adjacentFlowers = 0

            for bloom in bloomDay:
                if bloom <= midDay:
                    adjacentFlowers += 1
                    if adjacentFlowers == k:
                        bouquetsCount += 1
                        adjacentFlowers = 0
                else:
                    adjacentFlowers = 0

            if bouquetsCount >= m:
                rightDay = midDay
            else:
                leftDay = midDay + 1

        return leftDay