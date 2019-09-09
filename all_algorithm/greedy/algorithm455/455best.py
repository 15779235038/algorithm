#!/usr/bin/python3

# -*-coding:utf-8 -*-

#Reference:**********************************************

# @Time    : 2019/9/10 12:11 上午

# @Author  : baozhiqiang

# @File    : 455best.py

# @User    : bao

# @Software: PyCharm

#Reference:**********************************************


class Solution:
    def findContentChildren(self, g, s):
        if  not g or (not s):
            return 0
        s = sorted(s)
        g = sorted(g)
        number = 0
        index = 0
        for s_every in range(len(s)):
            if s[s_every] >= g[index]:
                index += 1
                number += 1
            if index == len(g):
                break


        return number











test = Solution()

print(test.findContentChildren([1, 2], [1, 2, 3]))
