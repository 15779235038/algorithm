#!/usr/bin/python3

# -*-coding:utf-8 -*-

#Reference:**********************************************

# @Time    : 2019/9/3 7:39 下午

# @Author  : Vicky.Yang

# @File    : 315best.py

# @User    : bao

# @Software: PyCharm

#Reference:**********************************************
# python 使用类创建结构体
class Myclass(object):
    class Struct(object):
        def __init__(self, name, age, job):
            self.name = name
            self.age = age
            self.job = job

    def make_struct(self, name, age, job):
        return self.Struct(name, age, job)



from collections import  defaultdict

class Solution:
    def countSmaller(self, nums):
        '''

        思路1：每次到某个元素就对后面进行二分查找。找到比它小的元素，
        :param nums:
        :return:
        '''
        nums_dict = defaultdict(int)
        for i  in range(0,len(nums)):
            #进行二分查找
            left = i
            right = len(nums) - 1
            mid = (right - left) // 2
            if nums[i] >mid:
                mid











test  =  Solution()
test.countSmaller([1,34,55,22,23])