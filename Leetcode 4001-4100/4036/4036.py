# Leetcode 4036: Lexicographically Largest String After Pair Transformations
# https://leetcode.com/problems/lexicographically-largest-string-after-pair-transformations/
# Solved on 28th of September, 2026
class Solution:
    def largestString(self, nums: list[int]) -> list[str]:
        """
        Transforms each initial character count into the lexicographically largest obtainable string.

        Parameters:
            nums (list[int]): A list of integers where each integer represents the count of initial 'a' characters.

        Returns:
            list[str]: The lexicographically largest strings corresponding to each input count.
        """
        charLookup = [chr(ord("a") + index) for index in range(26)]
        zBlockSize = 1 << 25
        resultList = []

        for numVal in nums:
            zCount = numVal >> 25
            remVal = numVal & (zBlockSize - 1)
            stringParts = ["z"] * zCount

            while remVal > 0:
                highestBit = remVal.bit_length() - 1
                stringParts.append(charLookup[highestBit])
                remVal ^= 1 << highestBit

            resultList.append("".join(stringParts))

        return resultList