// Leetcode 3646: Next Special Palindrome Number
// https://leetcode.com/problems/next-special-palindrome-number/
// Solved on 19th of December, 2025
import java.util.*;

class Solution {
    /**
     * Finds the next special palindrome number greater than the given number n.
     * A special palindrome number is a palindrome where the count of each digit is equal to the digit itself.
     * @param n The given long integer.
     * @return The smallest special palindrome number strictly greater than n, or -1 if none exists within reasonable bounds.
     */
    public long specialPalindrome(long n) {
        List<Long> candidates = new ArrayList<>();
        searchSubsets(1, 0, new ArrayList<>(), candidates);
        
        Collections.sort(candidates);
        
        for (long cand : candidates) {
            if (cand > n) {
                return cand;
            }
        }
        return -1;
    }

    private void searchSubsets(int currentDigit, int oddCount, List<Integer> currentSet, List<Long> candidates) {
        if (currentDigit > 9) {
            if (!currentSet.isEmpty()) {
                generatePalindromes(currentSet, candidates);
            }
            return;
        }

        searchSubsets(currentDigit + 1, oddCount, currentSet, candidates);

        boolean isOdd = (currentDigit % 2 != 0);
        if (isOdd && oddCount >= 1) {
            return;
        }

        currentSet.add(currentDigit);
        searchSubsets(currentDigit + 1, isOdd ? oddCount + 1 : oddCount, currentSet, candidates);
        currentSet.remove(currentSet.size() - 1);
    }

    private void generatePalindromes(List<Integer> distinctDigits, List<Long> candidates) {
        List<Integer> halfList = new ArrayList<>();
        int midDigit = -1;
        int totalLen = 0;

        for (int d : distinctDigits) {
            totalLen += d;
            if (d % 2 != 0) {
                midDigit = d;
                for (int k = 0; k < d / 2; k++) {
                    halfList.add(d);
                }
            } else {
                for (int k = 0; k < d / 2; k++) {
                    halfList.add(d);
                }
            }
        }
        
        if (totalLen > 18) {
            return;
        }

        Collections.sort(halfList);

        do {
            StringBuilder sb = new StringBuilder();
            for (int d : halfList) {
                sb.append(d);
            }
            
            String left = sb.toString();
            String right = sb.reverse().toString();
            String full = left + (midDigit != -1 ? midDigit : "") + right;
            
            try {
                candidates.add(Long.parseLong(full));
            } catch (NumberFormatException e) {
                // Ignore if it somehow overflows Long, though length check prevents most
            }

        } while (nextPermutation(halfList));
    }

    private boolean nextPermutation(List<Integer> list) {
        int i = list.size() - 2;
        while (i >= 0 && list.get(i) >= list.get(i + 1)) {
            i--;
        }
        if (i < 0) {
            return false;
        }

        int j = list.size() - 1;
        while (list.get(j) <= list.get(i)) {
            j--;
        }

        Collections.swap(list, i, j);
        Collections.reverse(list.subList(i + 1, list.size()));
        return true;
    }
}