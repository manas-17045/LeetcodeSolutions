# Leetcode 3303: Find the Occurrence of First Almost Equal Substring
# https://leetcode.com/problems/find-the-occurrence-of-first-almost-equal-substring/
# Solved on 23rd of June, 2025
import numpy as np

class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        """
        Finds the minimum starting index in string `s` such that the substring
        s[i...i+m-1] is "almost equal" to `pattern`.

        Two strings are "almost equal" if they differ by at most one character.
        This problem is solved using Fast Fourier Transform (FFT) to efficiently
        calculate the number of matching characters between substrings of `s`
        and `pattern`.

        Args:
            s (str): The main string to search within.
            pattern (str): The pattern string to find.
        Returns:
            int: The minimum starting index `i` in `s` where s[i...i+m-1] is
                 almost equal to `pattern`, or -1 if no such substring exists.
        """
        n = len(s)
        m = len(pattern)

        # Determine FFT calculation length
        fftCalcLength = 1
        while fftCalcLength < n + m - 1:
            fftCalcLength *= 2

        # this array will store the sum of convolutions.
        cumulativeMatchesConvolution = np.zeros(fftCalcLength, dtype=float)

        sCharsArray = np.array(list(s))
        patternCharsArray = np.array(list(pattern))

        # Optimization: Iterate only over characters present in the pattern.
        uniqueCharsInPattern = set(patternCharsArray)

        for charValue in uniqueCharsInPattern:
            sBinary = (sCharsArray == charValue).astype(float)

            # patternBinaryReversed[k] = 1 if pattern[m - 1 - k] == charValue else 0
            patternBinaryReversed = (patternCharsArray[(m - 1)::-1] == charValue).astype(float)

            # Compute FFTs
            sFft = np.fft.fft(sBinary, n=fftCalcLength)
            patternFft = np.fft.fft(patternBinaryReversed, n=fftCalcLength)

            # Multiply in frequency domain (element-wise product)
            convolutionInFreqDomain = sFft * patternFft

            # Inverse FFT to get convolution result in time domain
            charSpecificConvolution = np.fft.ifft(convolutionInFreqDomain)

            # Add the real part of this character's convolution to the total.
            cumulativeMatchesConvolution += charSpecificConvolution.real

        # Check each possible starting position in s
        # The convolution result at index (m - 1 + i) corresponds to the window s[i...(i + m - 1)] vs pattern.
        for i in range(n - m + 1):
            # Number of exact character matches for substring s[i:(i + m)] wth pattern.
            numberOfMatches = round(cumulativeMatchesConvolution[m - 1 + i])

            if numberOfMatches >= m - 1:
                return i

        return -1