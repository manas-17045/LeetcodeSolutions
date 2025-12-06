// Leetcode 3115: Maximum Prime Difference
// https://leetcode.com/problems/maximum-prime-difference/
// Solved on 6th of December, 2025
class Solution {
    /**
     * Finds the maximum difference between the indices of two prime numbers in the given array.
     * @param nums The input array of integers.
     * @return The maximum difference between the indices of the first and last prime numbers found.
     */
    public int maximumPrimeDifference(int[] nums) {
        int leftIndex = 0;
        int rightIndex = nums.length - 1;

        while (leftIndex <= rightIndex) {
            if (isPrime(nums[leftIndex])) {
                break;
            }
            leftIndex++;
        }

        while (rightIndex >= leftIndex) {
            if (isPrime(nums[rightIndex])) {
                break;
            }
            rightIndex--;
        }

        return rightIndex - leftIndex;
    }

    private boolean isPrime(int number) {
        if (number <= 1) {
            return false;
        }
        for (int i = 2; i * i <= number; i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
}