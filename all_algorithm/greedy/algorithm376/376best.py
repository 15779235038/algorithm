#!/usr/bin/python3

# -*-coding:utf-8 -*-

#Reference:**********************************************

# @Time    : 2019/9/30 12:06 上午

# @Author  : baozhiqiang

# @File    : 376best.py

# @User    : bao

# @Software: PyCharm

#Reference:**********************************************

class Solution:
    def wiggleMaxLength(self, nums):
        '''


        :param nums:
        :return:
        '''

        if len(nums) <2:
            return len(nums)
        prevdiff = nums[1] - nums[0]
        count = None
        if prevdiff !=0:
            count = 2
        else:
            count = 1


        for i in range(2,len(nums)):
            dif =nums[i]- nums[i-1]
            if dif>0 and prevdiff <= 0 or (dif<0 and prevdiff >=0) :
                count += 1
                prevdiff =dif

        return count


test =Solution()
print(test.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))