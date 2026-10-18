// Leetcode 4053: Minimum Operations to Make Every Element Palindromic
// https://leetcode.com/problems/minimum-operations-to-make-every-element-palindromic/
// Solved on 18th of October, 2026
class Solution {
    /**
     * Calculates the minimum number of increment or decrement by 2 operations required
     * to transform every element in the array into a positive palindromic integer.
     *
     * @param nums the input array of positive integers
     * @return the minimum total number of operations required
     */
    public long minOperations(int[] nums) {
        long totalOperations = 0;

        for (int num : nums) {
            if (num < 10) {
                continue;
            }

            long value = num;
            long tempValue = value;
            int digitCount = 0;
            long highestPower = 1;

            while (tempValue >= 10) {
                tempValue /= 10;
                digitCount++;
                highestPower *= 10;
            }
            digitCount++;
            long firstDigit = tempValue;

            long lowerPalindrome;
            long upperPalindrome;

            if ((firstDigit & 1) != (value & 1)) {
                if (firstDigit == 1) {
                    lowerPalindrome = (digitCount == 2) ? 8 : (highestPower - 1) - (highestPower / 10 + 1);
                } else {
                    long prevDigit = firstDigit - 1;
                    lowerPalindrome = (highestPower * 10 - 1) - (9 - prevDigit) * (highestPower + 1);
                }

                if (firstDigit == 9) {
                    upperPalindrome = 2 * (highestPower * 10 + 1);
                } else {
                    long nextDigit = firstDigit + 1;
                    upperPalindrome = nextDigit * (highestPower + 1);
                }
            } else {
                int rightDigits = digitCount / 2;
                long divisor = 1;
                for (int i = 0; i < rightDigits; i++) {
                    divisor *= 10;
                }

                long prefix = value / divisor;
                long middlePalindrome = prefix;
                long mirrorSource = (digitCount % 2 == 1) ? (prefix / 10) : prefix;
                for (int i = 0; i < rightDigits; i++) {
                    middlePalindrome = middlePalindrome * 10 + (mirrorSource % 10);
                    mirrorSource /= 10;
                }

                if (middlePalindrome == value) {
                    continue;
                } else if (middlePalindrome < value) {
                    lowerPalindrome = middlePalindrome;
                    long maxSameDigitPalindrome = (highestPower * 10 - 1) - (9 - firstDigit) * (highestPower + 1);

                    if (middlePalindrome == maxSameDigitPalindrome) {
                        upperPalindrome = (firstDigit + 2) * (highestPower + 1);
                    } else {
                        long nextPrefix = prefix + 1;
                        upperPalindrome = nextPrefix;
                        long nextMirror = (digitCount % 2 == 1) ? (nextPrefix / 10) : nextPrefix;
                        for (int i = 0; i < rightDigits; i++) {
                            upperPalindrome = upperPalindrome * 10 + (nextMirror % 10);
                            nextMirror /= 10;
                        }
                    }
                } else {
                    upperPalindrome = middlePalindrome;
                    long minSameDigitPalindrome = firstDigit * (highestPower + 1);

                    if (middlePalindrome == minSameDigitPalindrome) {
                        if (firstDigit == 2) {
                            lowerPalindrome = (digitCount == 2) ? 8 : (highestPower - 1) - (highestPower / 10 + 1);
                        } else {
                            long prevDigit = firstDigit - 2;
                            lowerPalindrome = (highestPower * 10 - 1) - (9 - prevDigit) * (highestPower + 1);
                        }
                    } else {
                        long prevPrefix = prefix - 1;
                        lowerPalindrome = prevPrefix;
                        long prevMirror = (digitCount % 2 == 1) ? (prevPrefix / 10) : prevPrefix;
                        for (int i = 0; i < rightDigits; i++) {
                            lowerPalindrome = lowerPalindrome * 10 + (prevMirror % 10);
                            prevMirror /= 10;
                        }
                    }
                }
            }

            long lowerDiff = value - lowerPalindrome;
            long upperDiff = upperPalindrome - value;
            totalOperations += Math.min(lowerDiff, upperDiff) / 2;
        }

        return totalOperations;
    }
}