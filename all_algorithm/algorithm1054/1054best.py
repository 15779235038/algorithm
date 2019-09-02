class Solution:

    '''
    思路：
        要想让相邻的元素不重复那么可以将相同的元素间隔一个一字儿排开，排到末尾再从头开始填空就行。

    统计元素出现次数，然后降序排序。依次从出现次数最多的元素的填入。
    '''
    def rearrangeBarcodes(self, barcodes):


