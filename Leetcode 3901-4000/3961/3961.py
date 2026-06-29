# Leetcode 3961: Maximize Sum of Device Ratings
# https://leetcode.com/problems/maximize-sum-of-device-ratings/
# Solved on 29th of June, 2026
class Solution:
    def maxRatings(self, units: list[list[int]]) -> int:
        """
        Computes the maximum sum of ratings for the devices.
        
        @param units: The input array of device ratings.
        @return: The maximum sum of ratings.
        """
        n = len(units[0])
        sumM1 = 0
        sumM2 = 0
        minM1 = float('inf')
        minM2 = float('inf')

        for deviceUnits in units:
            m1 = float('inf')
            m2 = float('inf')

            for u in deviceUnits:
                if u < m1:
                    m2 = m1
                    m1 = u
                elif u < m2:
                    m2 = u

            if n == 1:
                m2 = 0

            sumM1 += m1
            sumM2 += m2

            if m1 < minM1:
                minM1 = m1
            if m2 < minM2:
                minM2 = m2

        return max(sumM1, sumM2 - minM2 + minM1)