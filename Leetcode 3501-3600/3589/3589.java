// Leetcode 3589: Count Prime-Gap Balanced Subarrays
// https://leetcode.com/problems/count-prime-gap-balanced-subarrays/
// Solved on 30th of December, 2025
class Solution {
    /**
     * Counts the number of prime-gap balanced subarrays.
     * A subarray is prime-gap balanced if the difference between the maximum and minimum prime numbers within it is at most k.
     * @param nums The input integer array.
     * @param k The maximum allowed difference between the maximum and minimum prime numbers in a balanced subarray.
     * @return The total count of prime-gap balanced subarrays.
     */
    public int primeSubarray(int[] nums, int k) {
        int maxVal = 0;
        for (int num : nums) {
            maxVal = Math.max(maxVal, num);
        }

        boolean[] isPrime = new boolean[maxVal + 1];
        Arrays.fill(isPrime, true);
        if (maxVal >= 0) {
            isPrime[0] = false;
        }
        if (maxVal >= 1) {
            isPrime[1] = false;
        }
        for (int i = 2; i * i <= maxVal; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= maxVal; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        int n = nums.length;
        int[] primeVals = new int[n];
        int[] gaps = new int[n];
        int pCount = 0;
        int prevPrimeIdx = -1;

        Deque<Integer> maxDeque = new ArrayDeque<>();
        Deque<Integer> minDeque = new ArrayDeque<>();

        long totalCount = 0;
        long currentValid = 0;
        int left = 0;

        for (int i = 0; i < n; i++) {
            if (isPrime[nums[i]]) {
                primeVals[pCount] = nums[i];
                gaps[pCount] = i - prevPrimeIdx;

                if (pCount > 0) {
                    currentValid += gaps[pCount - 1];
                }

                while (!maxDeque.isEmpty() && primeVals[maxDeque.peekLast()] <= nums[i]) {
                    maxDeque.pollLast();
                }
                maxDeque.offerLast(pCount);

                while (!minDeque.isEmpty() && primeVals[minDeque.peekLast()] >= nums[i]) {
                    minDeque.pollLast();
                }
                minDeque.offerLast(pCount);

                while (!maxDeque.isEmpty() && !minDeque.isEmpty() && 
                       primeVals[maxDeque.peekFirst()] - primeVals[minDeque.peekFirst()] > k) {
                    currentValid -= gaps[left];
                    left++;
                    if (maxDeque.peekFirst() < left) {
                        maxDeque.pollFirst();
                    }
                    if (minDeque.peekFirst() < left) {
                        minDeque.pollFirst();
                    }
                }

                prevPrimeIdx = i;
                pCount++;
            }
            totalCount += currentValid;
        }

        return (int) totalCount;
    }
}