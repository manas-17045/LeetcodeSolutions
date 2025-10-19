// Leetcode 3216: Lexicographically Smallest String After a Swap
// https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/
// Solved on 19th of October, 2025
#include <string>
#include <algorithm>

class Solution {
public:    
    string getSmallestString(string s) {
        int stringLength = s.length();
        for (int i = 0; i < stringLength - 1; ++i) {
            bool haveSameParity = ((s[i] - '0') % 2) == ((s[i + 1] - '0') % 2):
            if (haveSameParity) {
                if (s[i] > s[i + 1]) {
                    std::swap(s[i], s[i + 1]);
                    break;
                }
            }
        }
        return s;
    }
}