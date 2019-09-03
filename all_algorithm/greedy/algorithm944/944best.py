#!/usr/bin/python3

# -*-coding:utf-8 -*-

#Reference:**********************************************

# @Time    : 2019/9/3 9:07 下午

# @Author  : Vicky.Yang

# @File    : 944best.py

# @User    : bao

# @Software: PyCharm

#Reference:**********************************************

class Solution(object):
    def minDeletionSize(self, A):
        ans = 0
        for col in zip(*A):
            print(col)
            if any(col[i] > col[i+1] for i in range(len(col) - 1)):
                ans += 1
        return ans



test = Solution()
print(test.minDeletionSize(["cba", "daf", "ghi"]))