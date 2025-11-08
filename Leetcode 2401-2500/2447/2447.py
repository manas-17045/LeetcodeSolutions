# Leetcode 2447: Number of Subarrays With GCD Equal to K
# https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/
# Solved on 8th of November, 2025
class Solution:
    def subarrayGCD(self, nums: list[int], k: int) -> int:
        """
        Calculates the number of subarrays in `nums` whose greatest common divisor (GCD) is equal to `k`.

        :param nums: A list of integers.
        :param k: The target GCD value.
        :return: The number of subarrays with GCD equal to `k`.
        """
        def getGcd(a, b):
            while b:
                a, b = b, a % b
            return a

        count = 0
        n = len(nums)

        for i in range(n):
            currentGcd = 0
            for j in range(i, n):
                if nums[j] % k != 0:
                    break

                currentGcd = getGcd(currentGcd, nums[j])

                if currentGcd == k:
                    count += 1

        return count