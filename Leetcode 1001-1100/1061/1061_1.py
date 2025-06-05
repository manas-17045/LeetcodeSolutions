# Leetcode 1061: Lexicographically Smallest Equivalent String
# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/
# Solved on 5th of June, 2025

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        """
        Given two strings s1 and s2 of equal length, we define a string s3 to be equivalent to s4 if,
        for all indices i, s3[i] and s4[i] are equivalent characters.
        Two characters a and b are equivalent if:
        - a == b, or
        - a is equivalent to c, and c is equivalent to b, or
        - a is equivalent to c, and b is equivalent to c.

        You are given two strings s1 and s2 of equal length and a base string baseStr.
        A character a is equivalent to a character b if s1[i] is equivalent to s2[i] for all indices i.
        Return the lexicographically smallest string equivalent to baseStr.

        This problem can be solved using the Union-Find data structure.
        """
        parent = list(range(26))

        def charToInt(c: str) -> int:
            return ord(c) - ord('a')

        def intToChar(i: int) -> str:
            return chr(i + ord('a'))

        def findSet(i: int) -> int:
            if parent[i] == i:
                return i
            parent[i] = findSet(parent[i])
            return parent[i]

        def unionSets(i: int, j: int):
            rootI = findSet(i)
            rootJ = findSet(j)
            if rootI != rootJ:
                if rootI < rootJ:
                    parent[rootJ] = rootI
                else:
                    parent[rootI] = rootJ

        for k in range(len(s1)):
            char1Val = charToInt(s1[k])
            char2Val = charToInt(s2[k])
            unionSets(char1Val, char2Val)

        resultChars = []
        for charBase in baseStr:
            charBaseVal = charToInt(charBase)
            rootVal = findSet(charBaseVal)
            resultChars.append(intToChar(rootVal))

        return "".join(resultChars)