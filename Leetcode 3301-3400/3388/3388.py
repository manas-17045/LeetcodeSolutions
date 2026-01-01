# Leetcode 3388: Count Beautiful Splits in an Array
# https://leetcode.com/problems/count-beautiful-splits-in-an-array/
# Solved on 1st of January, 2025
class Solution:
    def beautifulSplits(self, nums: list[int]) -> int:
        """
        Counts the number of beautiful splits in the given array.

        Args:
            nums: The input list of integers.
        Returns:
            The total count of beautiful splits.
        """
        n = len(nums)

        def getZ(start):
            length = n - start
            z = [0] * length
            l, r = 0, 0

            for i in range(1, length):
                if i <= r:
                    z[i] = min(r - i + 1, z[i - l])

                while i + z[i] < length and nums[start + z[i]] == nums[start + i + z[i]]:
                    z[i] += 1

                if i + z[i] - 1 > r:
                    l, r = i, i + z[i] - 1

            z[0] = length
            return z

        zMain = getZ(0)
        ans = 0

        for i in range(1, n - 1):
            isNums1Prefix = zMain[i] >= i
            zSuffix = getZ(i)

            for j in range(i + 1, n):
                len2 = j - i

                if isNums1Prefix and i <= len2:
                    ans += 1
                else:
                    if len2 <= n - j:
                        if zSuffix[j - i] >= len2:
                            ans += 1

        return ans