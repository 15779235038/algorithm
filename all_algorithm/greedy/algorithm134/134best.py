#!/usr/bin/python3

# -*-coding:utf-8 -*-

#Reference:**********************************************

# @Time    : 2019/9/28 11:03 下午

# @Author  : baozhiqiang

# @File    : 134best.py

# @User    : bao

# @Software: PyCharm

#Reference:**********************************************



class Solution:
    def canCompleteCircuit(self, gas, cost):
        '''

        思路：牛逼啊，只要O（n）就可以搞定的问题，太牛逼了。利用计数来记忆化之前的东西。


        :param gas:
        :param cost:
        :return:
        '''
        n = len(gas)
        total_tank, curr_tank = 0, 0
        starting_station = 0
        for i in range(n):
            total_tank += gas[i] - cost[i] #所有的油,它是不变的，
            print('total_tank',total_tank)
            curr_tank += gas[i] - cost[i]  #当前的油 ，排除不能作为加油站的点，
            print('curr_tank',curr_tank)
            # If one couldn't get here,
            if curr_tank < 0:   #排除当前点，并更新curr——tank为0，从下一个点开始，如果 total_tank 》
                #0，就证明可以
                # Pick up the next station as the starting one.
                starting_station = i + 1
                # Start with an empty tank.
                curr_tank = 0

        return starting_station if total_tank >= 0 else -1





test = Solution()
print(test.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))