#!/usr/bin/python3

# -*-coding:utf-8 -*-

#Reference:**********************************************

# @Time    : 2019/10/2 5:02 下午

# @Author  : baozhiqiang

# @File    : 435best.py

# @User    : bao

# @Software: PyCharm

#Reference:**********************************************


class Solution:
    def eraseOverlapIntervals(self, intervals):
        '''
        思路：贪心删除去那些跨度大的。直到剩下的list不会交界。
        '''
        count = 0
        curr = 0
        index = 1
        intervals = sorted(intervals, key=lambda x: x[0])
        if len(intervals) == 0:
            return 0
        # print('len(intervals)',len(intervals))
        while index != len(intervals):
            if intervals[index - 1][1] <= intervals[index][0]:
                # index = index
                pass
            elif intervals[index - 1][0] <= intervals[index][0] and (intervals[index][1] <= intervals[index - 1][1]):
                # curr = index
                count += 1
            else:
                intervals.remove(intervals[index])
                index -= 1
                count += 1
            index += 1
        # print(count)
        return count
        # pass







test = Solution()
test.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]])
