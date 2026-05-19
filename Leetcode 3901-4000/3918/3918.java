// Leetcode 3918: Sum of Primes Between Number and Its Reverse
// https://leetcode.com/problems/sum-of-primes-between-number-and-its-reverse/
// Solved on 19th of May, 2026
class Solution {
    /**
     * Calculates the sum of all prime numbers between a given integer and its reverse.
     * 
     * @param n The input integer.
     * @return The sum of prime numbers in the range [min(n, reverse(n)), max(n, reverse(n))].
     */
    public int sumofPrimesInRange(int n) {
        int reversedNumber = 0;
        int tempNumber = n;
        while (tempNumber > 0) {
            reversedNumber = reversedNumber * 10 + tempNumber % 10;
            tempNumber /= 10;
        }
        
        int rangeStart = Math.min(n, reversedNumber);
        int rangeEnd = Math.max(n, reversedNumber);
        
        if (rangeEnd < 2) {
            return 0;
        }
        
        boolean[] isComposite = new boolean[rangeEnd + 1];
        for (int i = 2; i * i <= rangeEnd; i++) {
            if (!isComposite[i]) {
                for (int j = i * i; j <= rangeEnd; j += i) {
                    isComposite[j] = true;
                }
            }
        }
        
        int primeSum = 0;
        int effectiveStart = Math.max(2, rangeStart);
        for (int i = effectiveStart; i <= rangeEnd; i++) {
            if (!isComposite[i]) {
                primeSum += i;
            }
        }
        
        return primeSum;
    }
}