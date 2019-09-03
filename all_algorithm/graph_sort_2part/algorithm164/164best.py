'''
因为追求线性复杂度，所以不可能用经典排序的算法，因此需要更巧妙地利用已知条件。
 类似与抽屉原理。我们用O(n)预处理出数组的最大值maxn和最小值minn，那么最大的间距
 肯定在maxn-minn之间，有因为有n个数，所以每个数之间的平均距离为size=(maxn-minn)/n+1,
 这是如果数组有序且元素都是等间距的时候的最大间距。因此我们一共要把数组按每个元素与最小
 值minn的间距大小分为(maxn-minn)/size+1个小组。每个组中保存组里面的最大值和最小值。
 那么对最后分到数的分组来说，整体的最大间距就是每个有效的分组的最小值减去前一个分组的最大值。





'''


'''
选择合适的桶大小 bb 满足 1 < b \leq (max - min)/(n-1)1<b≤(max−min)/(n−1)。
设 b = \lfloor (max - min)/(n-1) \rfloorb=⌊(max−min)/(n−1)⌋。
所有 nn 个元素被分为 k = \lceil (max - min)/b \rceilk=⌈(max−min)/b⌉ 个桶。
因此第 ii 个桶保存的值区间为：\bigg [min + (i-1) * b, \space min + i*b \bigg )[min+(i−1)∗b, min+i∗b)（下标从 1 开始）。
显然很容易计算出每个元素属于哪个桶，\lfloor (num - min)/b \rfloor⌊(num−min)/b⌋（下标从 0 开始）其中 numnum 是元素的值。
当所有 nn 个元素都遍历过后，比较 k-1k−1 个相邻桶找到最大间距。



'''

class Solution:
    def maximumGap(self, nums):
        maxs =max(nums)
        mins = min(nums)
        #选择合适桶大小。
        b = (maxs-mins) // (len(nums) - 1)
        print(b)
        #看下桶多少
        k = (maxs -mins) // b

        #放入k个桶，制造k个桶。
        tong = [[] for i in range(0,k)]
        print(tong)
        for j in nums:
            tong[(j- mins) // b].append(j)
        print(tong)








test = Solution()
test.maximumGap([34,36,3,76,98])
