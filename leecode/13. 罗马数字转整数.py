'''
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

示例 1:

输入: "III"
输出: 3
'''


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
        sums, lens = 0, len(s)
        for i in range(lens-1):
            if roman[s[i]] < roman[s[i+1]]:
                sums -= roman[s[i]]
            else:
                sums += roman[s[i]]
        return sums + roman[s[-1]]
