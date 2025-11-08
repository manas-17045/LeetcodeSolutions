# Leetcode 2470: Number of Subarrays With LCM Equal to K
# https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/
# Solved on 8th of November, 2025
class Solution:
    def subarrayLCM(self, nums: list[int], k: int) -> int:
        """
        Calculates the number of subarrays in `nums` whose least common multiple (LCM) is equal to `k`.

        Args:
            nums (list[int]): The input list of integers.
            k (int): The target LCM value.
        Returns:
            int: The number of subarrays with LCM equal to `k`.
        """
        def getGcd(a, b):
            while b:
                a, b = b, a % b
            return a

        count = 0
        n = len(nums)

        for i in range(n):
            currentLcm = 1
            for j in range(i, n):

                num = nums[j]

                if k % num != 0:
                    break

                currentLcm = (currentLcm * num) // getGcd(currentLcm, num)

                if currentLcm > k:
                    break

                if currentLcm == k:
                    count += 1

        return count