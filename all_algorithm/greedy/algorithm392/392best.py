
#!/usr/bin/python3

# -*-coding:utf-8 -*-

#Reference:**********************************************

# @Time    : 2019/9/3 10:33 下午

# @Author  : Vicky.Yang

# @File    : 392best.py

# @User    : bao

# @Software: PyCharm

#Reference:**********************************************


class Solution:
    def isSubsequence(self, s, t):
        print(len(s))
        t = list(t)
        s = list(s)
        if len(s) == 0:
            return True
        a = 0
        for i in range(len(t)):
            if t[i] == s[a]:
                a += 1
            if a == len(s):
                return True
        return False

        # print(t)




test =Solution()
print(test.isSubsequence(s = "abc", t = "ahbgdc"))
