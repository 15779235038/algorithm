#!/usr/bin/python3

# -*-coding:utf-8 -*-

#Reference:**********************************************

# @Time    : 2019/10/3 2:28 下午

# @Author  : baozhiqiang

# @File    : 763best.py

# @User    : bao

# @Software: PyCharm

'''
        思路：
        1 统计每个元素出现的次数。
        2 然后遍历数组，每到一个元素，除了执行正常的-1，还要统计当前是否
        所有的元素都出现次数为0了，为0就截止这里，为第一个list
        '''
#Reference:**********************************************
from collections import  defaultdict
class Solution:
    def partitionLabels(self, S):

        if len(S) ==  0:
            return 0
        s_list = list(S)
        str_number = defaultdict(int)
        for str  in s_list:
            str_number[str] += 1
        print('str_number',str_number)
        count = 0
        temp_strlist = []
        result_list = []
        for  i  in s_list:
             temp_strlist.append(i)
             str_number[i] -= 1
             count += 1
             #检查当前所有出现的元素的出现次数是否都为0，
             flag= True
             for temp_str in temp_strlist:
                 if str_number[temp_str] !=0:
                    flag =False
             if flag:
                 result_list.append(count)
                 temp_strlist.clear()
                 count = 0

        print(result_list)
        return result_list


test =Solution()
print(test.partitionLabels("ababcbacadefegdehijhklij"))



