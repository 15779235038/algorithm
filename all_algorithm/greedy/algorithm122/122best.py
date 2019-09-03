#!/usr/bin/python3

# -*-coding:utf-8 -*-

#Reference:**********************************************

# @Time    : 2019/9/3 10:06 下午

# @Author  : Vicky.Yang

# @File    : 122best.py

# @User    : bao

# @Software: PyCharm

#Reference:**********************************************

class Solution:
    def maxProfit(self, prices):
        # 分别找到局部底值，高值。
        i = 0
        valley = prices[0]
        peak = prices[0]
        maxprofitsss = 0
        while i < len(prices)-1:
            while i <len(prices) -1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i] #找谷底
            while i < len(prices) -1 and prices[i] <= prices[i + 1]:
                 i += 1
            peak = prices[i]
            maxprofitsss += peak - valley

        print(maxprofitsss)










test = Solution()
test.maxProfit([4,6,2,3,4,5,3])
