# Given a string s, find the length of the longest substring without duplicate characters.
#
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
#
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        substring_chars = set()
        i = 0
        while i < len(s):
            for j in range(i, len(s)):
                if s[j] in substring_chars:
                    if len(substring_chars) > max_len:
                        max_len = len(substring_chars)
                    i += 1
                    substring_chars = set()
                    break
                else:
                    substring_chars.add(s[j])
        return max_len


if __name__ == "__main__":
    s = "abcabcbb"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))