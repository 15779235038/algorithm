
from  first import *
class Solution:
    def merge(self, intervals):

        if  len(intervals) == 1 :
            return intervals
        #先将数组进行按照第一位的排序。
        sore_1_list = self.shell_sort(intervals)
        print(sore_1_list)
        result_list = []
        # result_list.append()
        for j in range(0, len(intervals)-1):
            if (intervals[j+1][0]  > intervals[j][0]  or  intervals[j+1][0]  == intervals[j][0]) and (intervals[j+1][0]  > intervals[j][1] or  intervals[j+1][0]  == intervals[j][1]):
                print('#可以合并的。'+str(intervals[j+1]) +'   '+str(intervals[j]))
                result_list.append([intervals[j][0], intervals[j+1][1]])
            else:
                if j == 0:
                    result_list.append(intervals[0])
                print('不要合并'+str(intervals[j]))
                result_list.append(intervals[j+1])
        return result_list






    def shell_sort(self,lists):
        #增量序列
        n = len(lists)
        # temp_list = [i for i in range(0,n) if n/2 ]
        h = 0
        while h < n or h == n:
            h = 3 * h + 1
        print('生成初始增量'+str(h))
        while h > 1 or h == 1:
            for i in range(h, n):
                j = i - h
                temp = lists[i][0]
                temp1 = lists[i]   #根据首项交换
                while (j > 0  or j == 0) and lists[j][0] > temp  :
                    lists[j+h] = lists[j]
                    j = j - h
                lists[j + h] = temp1

            h = (h-1) // 3  # 递减增量
            print('递减的增量变成了'+str(h))
        return lists




test = Solution()
print(test.merge([[1, 4], [5, 6]]))

