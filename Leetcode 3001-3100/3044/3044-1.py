# Leetcode 3044: Most Frequent Prime
# https://leetcode.com/problems/most-frequent-prime/
# Solved on 16th of September, 2025
class Solution:
    def mostFrequentPrime(self, mat: list[list[int]]) -> int:
        """
        Finds the most frequent prime number formed by concatenating digits in all eight directions
        starting from each cell in the given matrix.
        :param mat: A 2D list of integers representing the matrix.
        :return: The most frequent prime number. If there are multiple such primes, return the largest one. If no such prime exists, return -1.
        """
        m = len(mat)
        n = len(mat[0])

        primeMemo = {}

        def isPrime(num):
            if num in primeMemo:
                return primeMemo[num]
            if num <= 1:
                primeMemo[num] = False
                return False
            i = 2
            while i * i <= num:
                if num % i == 0:
                    primeMemo[num] = False
                    return False
                i += 1
            primeMemo[num] = True
            return True

        freqMap = {}

        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

        for row in range(m):
            for col in range(n):
                for dr, dc in directions:
                    currentNumber = mat[row][col]
                    nextRow, nextCol = row + dr, col + dc

                    while 0 <= nextRow < m and 0 <= nextCol < n:
                        currentNumber = currentNumber * 10 + mat[nextRow][nextCol]
                        freqMap[currentNumber] = freqMap.get(currentNumber, 0) + 1
                        nextRow += dr
                        nextCol += dc

        maxFreq = 0
        ans = -1

        sortedNumbers = sorted(freqMap.keys())

        for num in sortedNumbers:
            if num > 10 and isPrime(num):
                freq = freqMap[num]
                if freq >= maxFreq:
                    maxFreq = freq
                    ans = num

        return ans