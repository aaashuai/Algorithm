'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
'''


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        s = strs[0]
        lens = len(s)

        while lens > 0:
            flag = True
            for i in strs[1:]:
                if s != i[:lens]:
                    s, lens, flag = s[:-1], (lens - 1), False
                    break
            if flag:
                break
        return s
