# Leetcode 3800: Minimum Cost to Make Two Binary Strings Equal
# https://leetcode.com/problems/minimum-cost-to-make-two-binary-strings-equal/
# Solved on 9th of January, 2026
class Solution:
    def minimumCost(self, s: str, t: str, flipCost: int, swapCost: int, crossCost: int) -> int:
        """
        Calculates the minimum cost to make two binary strings s and t equal.

        Args:
            s (str): The first binary string.
            t (str): The second binary string.
            flipCost (int): The cost to flip a single character (0 to 1 or 1 to 0).
            swapCost (int): The cost to swap two characters at different indices (s[i] and s[j]).
            crossCost (int): The cost to swap s[i] with t[i] (effectively flipping both s[i] and t[i] if they are different).

        Returns:
            int: The minimum cost to make s and t equal.
        """
        count01 = 0
        count10 = 0

        for chS, chT in zip(s, t):
            if chS != chT:
                if chS == '0':
                    count01 += 1
                else:
                    count10 += 1

        pairMixed = min(count01, count10)
        remaining = abs(count01 - count10)
        pairSame = remaining // 2
        oddOne = remaining % 2

        costMixed = min(swapCost, 2 * flipCost)
        costSame = min(crossCost + swapCost, 2 * flipCost)

        return (pairMixed * costMixed) + (pairSame * costSame) + (oddOne * flipCost)