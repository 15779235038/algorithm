#!/usr/bin/python3

# -*-coding:utf-8 -*-

#Reference:**********************************************

# @Time    : 2019/9/10 12:23 上午

# @Author  : baozhiqiang

# @File    : 860best.py

# @User    : bao

# @Software: PyCharm

#Reference:**********************************************

import  copy
class Solution:
    def lemonadeChange(self, bills):


        #仅仅用一个小变量，就可以轻易的将我们的10，5块钱记住，如果有的话，就-1，不然就加。聪明

        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five: return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True


test = Solution()
print(test.lemonadeChange([5,5,10,10,20]))
