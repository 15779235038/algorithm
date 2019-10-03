#!/usr/bin/python3

# -*-coding:utf-8 -*-

#Reference:**********************************************

# @Time    : 2019/10/3 10:35 上午

# @Author  : baozhiqiang

# @File    : 659best.py

# @User    : bao

# @Software: PyCharm

#Reference:**********************************************
from  collections import  defaultdict
class Solution:
    def isPossible(self, nums):
        # 记录元素出现次数
        counter = defaultdict(int)
        for n in nums:
            counter[n] +=1
        print('counter',counter)
        end =defaultdict(int)
        for i in nums:
            if counter[i] == 0:
                continue
            print(i)
            counter[i] -= 1
            if i - 1 in end.keys(): #存在以n-1结尾的连续子序列
                if end[i-1] > 0:
                    end[i-1] -= 1
                    end[i] += 1
                    print('end', end)

                elif i+1 in counter.keys() and i+2 in counter.keys(): #可以构成新的序列
                        if  counter[i+1] > 0 and counter[i+2]> 0:
                            # counter[i] -= 1
                            counter[i + 1] -= 1
                            counter[i + 2] -= 1
                            end[i + 2] += 1
                            print('endss',end)
                            print('sfdsfds')
                        else:
                                print('ssss')
                                return False
        return True






test =Solution()
print(test.isPossible([1,2,3,4,4,5]))