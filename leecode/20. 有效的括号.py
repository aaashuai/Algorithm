'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
'''


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {')': '(', ']': '[', '}': '{'}
        l = []
        for i in s:
            if not l or i not in brackets or (i in brackets and brackets[i] != l[-1]):
                l.append(i)
            else:
                l.pop(-1)
        return False if l else True
