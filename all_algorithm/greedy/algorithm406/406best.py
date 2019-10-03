#!/usr/bin/python3

# -*-coding:utf-8 -*-

#Reference:**********************************************

# @Time    : 2019/10/2 4:00 下午

# @Author  : baozhiqiang

# @File    : 406best.py

# @User    : bao

# @Software: PyCharm

#Reference:**********************************************

'''
插入排序思想，先排序，然后不断从后面到前面进行判断，移入的最佳位置。


'''
class Solution:
    def reconstructQueue(self, people):
        # 对 people 排序：按 h 降序，k 升序
        people.sort(key=lambda x: (-x[0], x[1]))
        length = len(people)
        print('people',people)
        i = 0
        while i < length:
            cur_people = people[i]
            print('curr_people',cur_people)
            k = cur_people[1]
            print('k',k)
            if k < i:
                # 从后往前遍历，进行「插队」步骤的元素交换
                for j in range(i, k, -1):
                    people[j] = people[j - 1]
                people[k] = cur_people
            i += 1
            print(people)
        print(people)
        return people






test =Solution()
test.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])


