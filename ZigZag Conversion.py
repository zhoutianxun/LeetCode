"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        out = []
        if numRows <= 1:
            return s
        for i in range(numRows):
            out.append("")

        for i in range(len(s)):
            # calculate row
            x = i % (2 * (numRows - 1))
            if x <= numRows - 1:
                row = x
            else:
                row = 2 * (numRows - 1) - x

            out[row] = out[row] + s[i]
        return "".join(out)
