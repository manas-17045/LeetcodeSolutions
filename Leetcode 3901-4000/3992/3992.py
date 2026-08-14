# Leetcode 3993: Rearrange String to Avoid Character Pair
# https://leetcode.com/problems/rearrange-string-to-avoid-character-pair/
# Solved on 14th of August, 2026
class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        """
        Rearranges the characters of a string such that no two identical characters are adjacent and no `x` is followed by a `y`. 

        Args:
            s: The input string.
            x: The first character.
            y: The second character.
        
        Returns:
            The rearranged string.
        """
        yChars = []
        otherChars = []
        xChars = []

        for currentChar in s:
            if currentChar == y:
                yChars.append(currentChar)
            elif currentChar == x:
                xChars.append(currentChar)
            else:
                otherChars.append(currentChar)

        return "".join(yChars + otherChars + xChars)