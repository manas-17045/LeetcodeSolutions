# Leetcode 3849: Maximum Bitwise XOR After Rearrangement
# https://leetcode.com/problems/maximum-bitwise-xor-after-rearrangement/
# Solved on 24th of February, 2026
class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        """
        Rearranges the characters of string t to maximize the bitwise XOR sum with string s.

        :param s: The reference binary string.
        :param t: The binary string whose characters can be rearranged.
        :return: The resulting binary string after XORing s with the optimally rearranged t.
        """
        countOnes = t.count('1')
        countZeros = len(t) - countOnes

        resultString = []
        for charValue in s:
            if charValue == '0':
                if countZeros > 0:
                    resultString.append('1')
                    countOnes -= 1
                else:
                    resultString.append('0')
                    countZeros -= 1
            else:
                if countZeros > 0:
                    resultString.append('1')
                    countZeros -= 1
                else:
                    resultString.append('0')
                    countOnes -= 1

        return "".join(resultString)