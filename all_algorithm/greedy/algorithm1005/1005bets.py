#!/usr/bin/python3

# -*-coding:utf-8 -*-

#Reference:**********************************************

# @Time    : 2019/9/11 6:33 下午

# @Author  : baozhiqiang

# @File    : 1005bets.py

# @User    : bao

# @Software: PyCharm

#Reference:**********************************************


class Solution:
    def largestSumAfterKNegations(self, A, K):

        '''
        将数据存入dict，
        '''
        index = 0
        num_order ={}
        for i in A:
            num_order[index] = i
            index += 1
        print(num_order)

        #进行排序，然后将负数全部反转，如果负数数量m<k,那么k-m都给予绝对值最小的值。比如有0那么k-m次0。







test = Solution()
test.largestSumAfterKNegations([3,43,5,6,3,2,1],2)