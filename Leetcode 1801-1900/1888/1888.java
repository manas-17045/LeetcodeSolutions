// Leetcode 1888: Minimum Number of Flips to Make the Binary String Alternating
// https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/
// Solved on 7th of March, 2026
class Solution {
    /**
     * Calculates the minimum number of flips to make a binary string alternating.
     * Type-1 operations (rotating the string) are allowed any number of times.
     * @param s A binary string consisting of '0's and '1's.
     * @return The minimum number of flips required.
     */
    public int minFlips(String s) {
        int n = s.length();
        int minFlips = Integer.MAX_VALUE;
        int diffOne = 0;
        int diffTwo = 0;
        
        for (int i = 0; i < 2 * n; i++) {
            char currentChar = s.charAt(i % n);
            char expectedOne = i % 2 == 0 ? '0' : '1';
            char expectedTwo = i % 2 == 0 ? '1' : '0';
            
            if (currentChar != expectedOne) {
                diffOne++;
            }
            if (currentChar != expectedTwo) {
                diffTwo++;
            }
            
            if (i >= n) {
                char removedChar = s.charAt((i - n) % n);
                char removedOne = (i - n) % 2 == 0 ? '0' : '1';
                char removedTwo = (i - n) % 2 == 0 ? '1' : '0';
                
                if (removedChar != removedOne) {
                    diffOne--;
                }
                if (removedChar != removedTwo) {
                    diffTwo--;
                }
            }
            
            if (i >= n - 1) {
                minFlips = Math.min(minFlips, Math.min(diffOne, diffTwo));
            }
        }
        
        return minFlips;
    }
}