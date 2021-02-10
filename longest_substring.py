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
        appeared_char = set()
        length = 0
        best = 0
        substr = ''
        best_substr = ''
        for char in s:
            if char in appeared_char:
                if length > best:
                    best_substr = substr
                    best = length
                    
                if char in substr:
                    substr = substr[substr.index(char)+1:] + char
                else:
                    substr += char
                length = len(substr)

            else:
                length += 1
                substr += char
                appeared_char.add(char)
        if length > best:
            best = length
        return best
            
