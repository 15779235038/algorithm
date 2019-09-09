#!/usr/bin/python3

# -*-coding:utf-8 -*-

#Reference:**********************************************

# @Time    : 2019/9/4 7:12 上午

# @Author  : baozhiqiang

# @File    : 1029best.py

# @User    : bao

# @Software: PyCharm

#Reference:**********************************************


class Solution:
    '''
    换个思路思考，找前n个去a最近的不就好了嘛

    '''
    def twoCitySchedCost(self, costs):
        costs.sort(key = lambda x : x[0] - x[1])
        total = 0
        n = len(costs) // 2
        # To optimize the company expenses,
        # send the first n persons to the city A
        # and the others to the city B
        for i in range(n):
            total += costs[i][0] + costs[i + n][1]
        return total





test  = Solution()
print(test.twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]))