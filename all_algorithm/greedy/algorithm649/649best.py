#!/usr/bin/python3

# -*-coding:utf-8 -*-

#Reference:**********************************************

# @Time    : 2019/10/3 10:05 上午

# @Author  : baozhiqiang

# @File    : 649best.py

# @User    : bao

# @Software: PyCharm

#Reference:**********************************************


class Solution:
    def predictPartyVictory(self, senate):
        R, D = True, True
        senate = list(senate)
        person = 0
        while R and D:
            R, D = False, False
            for i in range(len(senate)):
                if senate[i] == 'R':
                    R = True
                    if person < 0:
                        senate[i] = '0'
                    person += 1
                elif senate[i] == 'D':
                    D = True
                    if person > 0:
                        senate[i] = '0'
                    person -= 1
        return "Radiant" if person > 0 else "Dire"


test =Solution()
print(test.predictPartyVictory("RD"))

