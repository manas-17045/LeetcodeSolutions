// Leetcode 1415: The k-th Lexicographical String of All Happy Strings of Length n
// https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/
// Solved on 14th of March, 2026
class Solution {
    /**
     * Generates the k-th lexicographical happy string of length n.
     * A happy string consists only of ['a', 'b', 'c'] and no two adjacent characters are the same.
     *
     * @param n The length of the happy string.
     * @param k The lexicographical index (1-indexed) of the happy string to retrieve.
     * @return The k-th happy string, or an empty string if there are fewer than k happy strings.
     */
    public String getHappyString(int n, int k) {
        int total = 3 * (1 << (n - 1));
        if (k > total) {
            return "";
        }
        StringBuilder result = new StringBuilder();
        k--;
        int blockSize = 1 << (n - 1);
        int index = k / blockSize;
        char prev = (char) ('a' + index);
        result.append(prev);
        k %= blockSize;
        for (int i = 1; i < n; i++) {
            blockSize = 1 << (n - 1 - i);
            index = k / blockSize;
            char next;
            if (prev == 'a') {
                next = index == 0 ? 'b' : 'c';
            } else if (prev == 'b') {
                next = index == 0 ? 'a' : 'c';
            } else {
                next = index == 0 ? 'a' : 'b';
            }
            result.append(next);
            prev = next;
            k %= blockSize;
        }
        return result.toString();
    }
}