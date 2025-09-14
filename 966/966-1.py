# Leetcode 966: Vowel Spellchecker
# https://leetcode.com/problems/vowel-spellchecker/
# Solved on 14th of September, 2025
class Solution:
    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        """
        Implements a spellchecker that corrects queries based on a given wordlist.
        :param wordlist: A list of valid words.
        :param queries: A list of words to be spellchecked.
        :return: A list of corrected words, corresponding to each query.
        """
        def createVowelPattern(word):
            vowels = {'a', 'e', 'i', 'o', 'u'}
            return "".join(['*' if char in vowels else char for char in word.lower()])

        wordSet = set(wordlist)
        caseInsensitiveMap = {}
        vowelErrorMap = {}

        for word in wordlist:
            lowerWord = word.lower()
            if lowerWord not in caseInsensitiveMap:
                caseInsensitiveMap[lowerWord] = word

            pattern = createVowelPattern(word)
            if pattern not in vowelErrorMap:
                vowelErrorMap[pattern] = word

        resultList = []
        for query in queries:
            if query in wordSet:
                resultList.append(query)
                continue

            lowerQuery = query.lower()
            if lowerQuery in caseInsensitiveMap:
                resultList.append(caseInsensitiveMap[lowerQuery])
                continue

            queryPattern = createVowelPattern(query)
            if queryPattern in vowelErrorMap:
                resultList.append(vowelErrorMap[queryPattern])
                continue

            resultList.append("")

        return resultList