// Leetcode 1390: Four Divisors
// https://leetcode.com/problems/four-divisors/
// Solved on 4th of January, 2026
class Solution {
    /**
     * Calculates the sum of divisors for numbers that have exactly four divisors.
     * @param nums An array of integers.
     * @return The total sum of divisors for all numbers in `nums` that have exactly four divisors.
     */
    public int sumForDivisors(int[] nums) {
        int totalSum = 0;
        for (int num : nums) {
            int sum = 0;
            int count = 0;
            for (int i = 1; i * i <= num; i++) {
                if (num % i == 0) {
                    if (i * i == num) {
                        count++;
                        sum += i;
                    } else {
                        count += 2;
                        sum += i + num / i;
                    }
                    if (count > 4) {
                        break;
                    }
                }
            }
            if (count == 4) {
                totalSum += sum;
            }
        }
        return totalSum;
    }
}