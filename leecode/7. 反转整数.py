'''
给定一个 32 位有符号整数，将整数中的数字进行反转。

示例 1:

输入: 123
输出: 321
'''

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = x if x > 0 else -x
        res = 0

        while n:
            res = res * 10 + n % 10
            n //= 10

        if res > 2 ** 31:
            return 0
        return res if x > 0 else -res
