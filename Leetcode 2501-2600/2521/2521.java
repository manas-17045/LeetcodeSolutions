// Leetcode 2521: Distinct Prime Factors of Product of Array
// https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/
// Solved on 29th of November, 2025
import java.util.HashSet;
import java.util.Set;

class Solution {
    /**
     * Calculates the number of distinct prime factors of the product of all numbers in the input array.
     * @param nums The input array of integers.
     * @return The count of distinct prime factors.
     */
    public int distinctPrimeFactors(int[] nums) {
        Set<Integer> distinctPrimes = new HashSet<>();
        for (int num : nums) {
            if (num % 2 == 0) {
                distinctPrimes.add(2);
                while (num % 2 == 0) {
                    num /= 2;
                }
            }
            for (int i = 3; i * i <= num; i += 2) {
                if (num % i == 0) {
                    distinctPrimes.add(i);
                    while (num % i == 0) {
                        num /= i;
                    }
                }
            }
            if (num > 1) {
                distinctPrimes.add(num);
            }
        }
        return distinctPrimes.size();
    }
}