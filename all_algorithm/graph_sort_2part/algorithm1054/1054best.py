
from  collections import  defaultdict
class Solution:

    '''
    思路：
        要想让相邻的元素不重复那么可以将相同的元素间隔一个一字儿排开，排到末尾再从头开始填空就行。

    统计元素出现次数，然后降序排序。依次从出现次数最多的元素的填入。

    将相同的元素依次填入，然后重后往前填。
    '''
    def rearrangeBarcodes(self, barcodes):

        nums_dict = defaultdict(int)
        for   i  in barcodes:
            nums_dict[i] += 1

        #排序,降序排序
        sort_nums_dict = sorted(nums_dict.items(),key=lambda item: item[1], reverse= True)
        print(sort_nums_dict)
        #隔空填入
        result = [0 for i in range(0, len(barcodes))]
        # print(result)
        #
        k = 0
        temp = dict(sort_nums_dict)
        for key, value in temp.items():
                for i in range(0, value):
                    if k >len(result) -1:
                        break
                    else:
                        result[k] = key
                        k += 2
                        temp[key] -= 1


        k = 1
        for key,value  in temp.items():
            for i in range(0, value):
                if k > len(result) - 1:
                    break
                else:
                    result[k] = key
                    k += 2
                    temp[key] -= 1

        print(result)
        #再反把剩下的着填回去




test = Solution()
test.rearrangeBarcodes([1,1,1,1,2,2,3,3])






