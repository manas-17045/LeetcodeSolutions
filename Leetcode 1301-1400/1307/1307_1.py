# Leetcode 1307: Verbal Arithmetic Puzzle
# https://leetcode.com/problems/verbal-arithmetic-puzzle/
# Solved on 26th of July, 2025
class Solution:
    def isSolvable(self, words: list[str], result: str) -> bool:
        """
        Determines if a given verbal arithmetic puzzle is solvable.
        :param words: A list of strings representing the words to be summed.
        :param result: A string representing the target sum.
        :return: True if the puzzle is solvable, False otherwise.
        """

        allStrings = words + [result]
        reversedWords = [w[::-1] for w in words]
        reversedResult = result[::-1]

        maxLengthWord = 0
        if words:
            maxLengthWord = max(len(w) for w in words)

        if len(result) < maxLengthWord or len(result) > maxLengthWord + 1:
            return False

        charToDigit = {}
        digitUsed = [False] * 10

        leadingChars = set()
        for s in allStrings:
            if len(s) > 1:
                leadingChars.add(s[0])

        if len(set("".join(allStrings))) > 10:
            return False

        def solve(wordIndex, col, carry):
            if col == len(reversedResult):
                return carry == 0

            if wordIndex == len(words):
                resultChar = reversedResult[col]
                requiredDigit = carry % 10
                newCarry = carry // 10

                if resultChar in charToDigit:
                    if charToDigit[resultChar] == requiredDigit:
                        return solve(0, col + 1, newCarry)
                    return False
                else:
                    if digitUsed[requiredDigit] or (requiredDigit == 0 and resultChar in leadingChars):
                        return False

                    charToDigit[resultChar] = requiredDigit
                    digitUsed[requiredDigit] = True

                    if solve(0, col + 1, newCarry):
                        return True

                    del charToDigit[resultChar]
                    digitUsed[requiredDigit] = False
                    return False

            word = reversedWords[wordIndex]

            if col >= len(word):
                return solve(wordIndex + 1, col, carry)

            char = word[col]

            if char in charToDigit:
                return solve(wordIndex + 1, col, carry + charToDigit[char])
            else:
                for digit in range(10):
                    if not digitUsed[digit] and not (digit == 0 and char in leadingChars):
                        charToDigit[char] = digit
                        digitUsed[digit] = True

                        if solve(wordIndex + 1, col, carry + digit):
                            return True

                        del charToDigit[char]
                        digitUsed[digit] = False
                return False

        return solve(0, 0, 0)