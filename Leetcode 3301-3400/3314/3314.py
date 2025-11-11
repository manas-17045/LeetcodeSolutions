# Leetcode 3314: Construct the Minimum Bitwise Array I
# https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/
# Solved on 11th of November, 2025
class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        """
        Constructs the minimum bitwise array based on the given input numbers.

        :param nums: A list of integers.
        :return: A list of integers representing the constructed minimum bitwise array.
        """
        ans = []
        for num in nums:
            if num == 2:
                ans.append(-1)
            else:
                p = 0
                tempNum = num
                while (tempNum & 1) == 1:
                    tempNum >>= 1
                    p += 1

                val = num - (1 << (p - 1))
                ans.append(val)

        return ans