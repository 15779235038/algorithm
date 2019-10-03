#!/usr/bin/python3

# -*-coding:utf-8 -*-

#Reference:**********************************************

# @Time    : 2019/9/30 12:43 上午

# @Author  : baozhiqiang

# @File    : 402best.py

# @User    : bao

# @Software: PyCharm

#Reference:**********************************************

class Solution:
    def removeKdigits(self, nums, k):

        stack = []
        top = 0
        stack.append(nums[0])
        result = []
        for i  in nums:

            if k ==0:
                break

            if i >nums[top]:
                stack.append(i)
            else:
                result.append(stack.pop())
                k -= 1

test =Solution()
test.removeKdigits([])









