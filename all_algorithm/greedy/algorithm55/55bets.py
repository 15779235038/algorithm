#!/usr/bin/python3

# -*-coding:utf-8 -*-

#Reference:**********************************************

# @Time    : 2019/9/28 12:28 下午

# @Author  : baozhiqiang

# @File    : 55bets.py

# @User    : bao

# @Software: PyCharm

#Reference:**********************************************

class Solution:
    def canJump(self, nums):
        '''
        思路：
        1  反着来，从最后最后一个元素，反着来，如果从后往前数。
        有能够到第一个位置的元素，我们称为好元素。设置一个暂存变量，
        保留当前能够跳到的位置，
        '''

        test = [2,3,1,1,4]
        nums.reverse()
        temp = 0
        for index in range(nums):
            if index - nums[index] == temp:
                temp = index


























test = Solution()
test.canJump([])