'''
Given a string s, find the length of the longest substring without repeating characters.
---------------------------------------------------------------------------------------
Example:

>>> Input: s = "abcabcbb"
>>> Output: 3

Explanation: The answer is "abc", with the length of 3.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index = {}
        i, j, longest, = 0, 0, 0

        # move j down the string
        for j in range(len(s)):
            if s[j] in index and index[s[j]] >= i:
                i = index[s[j]] + 1
            index[s[j]] = j
            longest = max(longest, j-i+1)
        return longest
            
