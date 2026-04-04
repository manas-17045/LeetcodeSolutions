// Leetcode 2075: Decode the Slanted Ciphertext
// https://leetcode.com/problems/decode-the-slanted-ciphertext/
// Solved on 4th of Apil, 2026
class Solution {
    /**
     * Decodes a slanted ciphertext into its original string format.
     * @param encodedText The string representing the encoded grid.
     * @param rows The number of rows used in the slanted grid.
     * @return The decoded original string with trailing spaces removed.
     */
    public String decodeCipherText(String encodedText, int rows) {
        int len = encodedText.length();
        if (rows == 1 || len == 0) {
            return encodedText;
        }
        
        int cols = len / rows;
        StringBuilder sb = new StringBuilder();
        
        for (int col = 0; col < cols; col++) {
            for (int row = 0; row < rows; row++) {
                int currCol = col + row;
                if (currCol >= cols) {
                    break;
                }
                
                int idx = row * cols + currCol;
                sb.append(encodedText.charAt(idx));
            }
        }
        
        int end = sb.length() - 1;
        while (end >= 0 && sb.charAt(end) == ' ') {
            end--;
        }
        
        return sb.substring(0, end + 1);
    }
}