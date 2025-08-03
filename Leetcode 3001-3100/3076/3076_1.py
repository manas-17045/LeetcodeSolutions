# Leetcode 3076: Shortest Uncommon Substring in an Array
# https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/
# Solved on 3rd of August, 2025
import collections


class Solution:
    def shortestSubstrings(self, arr: list[str]) -> list[str]:
        """
        Finds the shortest uncommon substring for each word in the input array.

        An uncommon substring for a word is a substring that appears only in that word
        and not in any other word in the array. If multiple such substrings exist,
        the lexicographically smallest one is chosen.

        Args:
            arr: A list of strings.

        Returns:
            A list of strings, where each string is the shortest uncommon substring
            for the corresponding word in the input array. If no uncommon substring
            exists for a word, an empty string is returned.
        """
        subToIndices = collections.defaultdict(list)
        for i, word in enumerate(arr):
            wordLen = len(word)
            for subLen in range(1, (wordLen + 1)):
                for j in range(wordLen - subLen + 1):
                    sub = word[j:j + subLen]
                    subToIndices[sub].append(i)

        answer = []
        for i, word in enumerate(arr):
            wordLen = len(word)
            bestSub = ""

            for subLen in range(1, (wordLen + 1)):
                candidates = []
                for j in range(wordLen - subLen + 1):
                    sub = word[j:j + subLen]
                    if len(subToIndices[sub]) == 1:
                        candidates.append(sub)

                if candidates:
                    bestSub = min(candidates)
                    break

            answer.append(bestSub)

        return answer