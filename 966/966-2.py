# Leetcode 966: Vowel Spellchecker
# https://leetcode.com/problems/vowel-spellchecker/
# Solved on 14th of September, 2025
class Solution:
    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        """
        Implements a spellchecker that corrects query words based on a given wordlist.
        :param wordlist: A list of valid words.
        :param queries: A list of words to be spellchecked.
        :return: A list of corrected words, corresponding to each query.
        """
        vowels = set("aeiou")

        def deVowel(word: str) -> str:
            return "".join('*' if ch in vowels else ch for ch in word)

        # Exact words set
        exact_words = set(wordlist)

        # Case-insensitive dictionary: lowercase -> first occurrence
        case_insensitive = {}
        # Vowel-error dictionary: deVowel(lowercase) -> first occurrence
        vowel_insensitive = {}

        for word in wordlist:
            lower = word.lower()
            if lower not in case_insensitive:
                case_insensitive[lower] = word
            dev = deVowel(word)
            if dev not in vowel_insensitive:
                vowel_insensitive[dev] = word

        result = []
        for query in queries:
            if query in exact_words:
                result.append(query)
            else:
                lower = query.lower()
                if lower in case_insensitive:
                    result.append(case_insensitive[lower])
                else:
                    dev = deVowel(lower)
                    if dev in vowel_insensitive:
                        result.append(vowel_insensitive[dev])
                    else:
                        result.append("")

        return result