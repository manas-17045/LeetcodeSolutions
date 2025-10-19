# Leetcode 3216: Lexicographically Smallest String After a Swap
# https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/
# Solved on 19th of October, 2025
class Solution:
    def getSmallestString(self, s: str) -> str:
        """
        Given a string s, return the lexicographically smallest string after performing at most one swap.
        A swap can only be performed on two adjacent digits if they have the same parity (both even or both odd).

        :param s: The input string consisting of digits.
        :return: The lexicographically smallest string after at most one valid swap.
        """
        charList = list(s)
        length = len(charList)

        for i in range(length - 1):
            firstDigit = int(charList[i])
            secondDigit = int(charList[i + 1])

            if firstDigit % 2 == secondDigit % 2:
                if firstDigit > secondDigit:
                    charList[i], charList[i + 1] = charList[i + 1], charList[i]
                    return "".join(charList)

        return s