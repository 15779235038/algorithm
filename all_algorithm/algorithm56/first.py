#不好意思，这题我要手撕9大排序算法。

class Solution:
    def merge(self, intervals):
        # self.BubbleSore(intervals)

        print(self.shell_sort(intervals))
        pass


    '''
    冒泡排序
    '''
    def BubbleSore(self,lists):
        n = len(lists)
        flag = None
        for i in range(0, n):
            for j in range(0, n-1-i):
                flag = 1
                if lists[j] > lists[j+1]:
                    flag = 0
                    self.swap(lists, j, j+1)
            if flag:  break

    #交换两元素
    def  swap(self,lists, a, b):
        temp = lists[b]
        lists[b] = lists[a]
        lists[a] = temp

    '''
    
    鸡尾酒排序
    '''

    def cocktail_sort(self, l):
        print('原数据是'+str(l))
        l_len = len(l)
        for i in range(l_len, 0, -1):
            rem_i_l_len = abs(i - l_len)
            isNeedContinue = False
            obverse_count = len(l[rem_i_l_len: i - 1])
            print('obverse_count'+str(obverse_count))
            reverse_count = len(l[rem_i_l_len + 1: i - 1])
            print('reverse_count'+str(reverse_count))
            print('以下是正着排序')
            for j in range(obverse_count):
                if l[j] > l[j + 1]:
                    l[j], l[j + 1] = l[j + 1], l[j]   #交换两元素的python骚操作
                    isNeedContinue = True
            # you can print this to observe the whole process

            print (l)
            print('以下是反着排序的')
            for j in range(reverse_count, 0, -1):
                if l[j] < l[j - 1]:
                    l[j], l[j - 1] = l[j - 1], l[j]
                    isNeedContinue = True
            # you can print this to observe the whole process
            # print l
            print('判断还需要再排吗？')
            print (l)
            if isNeedContinue:
                continue
            else:
                return

    '''
    选择排序
    
    '''
    def  chose_sort(self,lists):
        #创建一个新lists，保存新的
        new_list = []
        n = len(lists)
        for i in range(0, n):
            #寻找当前最小
            if len(lists) != 0:
                mix = lists[0]
                temp = 0
                for j in range(0, len(lists)):
                     if lists[j] < mix:
                         mix = lists[j]
                         temp = j
                # 原数组弹出
                del lists[temp]
                new_list.append(mix)

        return new_list




    '''
    归并排序,非递归版本
    '''
    def merges(self,seq, low, mid, high):
        left = seq[low: mid]
        right = seq[mid: high]
        k = 0
        j = 0
        result = []
        while k < len(left) and j < len(right):
            if left[k] <= right[j]:
                result.append(left[k])
                k += 1
            else:
                result.append(right[j])
                j += 1
        result += left[k:]
        result += right[j:]
        seq[low: high] = result

        print(seq)


    '''
    合并排序的非递归版本
    '''
    def merge_sort(self,lists):
        i = 1  # i是步长
        while i < len(lists):
            low = 0
            #里面的while是实现两两合并的部分。
            while low < len(lists):
                mid = low + i  # mid前后均为有序
                high = min(low + 2 * i, len(lists))
                if mid < high:
                    self.merges(lists, low, mid, high)
                low += 2 * i
            i *= 2
        print(lists)



    '''
    合并排序的递归版本
    '''


    def merge2(self, a, b):
        c = []
        i = j = 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                c.append(a[i])
                i += 1
            else:
                c.append(b[j])
                j += 1
        while i < len(a):
            c.append(a[i])
            i += 1
        while j < len(b):
            c.append(b[j])
            j += 1
        return c

    def merge_sort2(self,lists):
        if len(lists) <= 1:
            return lists
        middle = len(lists) // 2
        left = self.merge_sort2(lists[:middle])
        right = self.merge_sort2(lists[middle:])
        return self.merge2(left, right)




    '''
    堆排序,不断输入到堆，维护堆的稳定，稳定后输出堆顶元素。
    '''


    import random

    def MAX_Heapify(self,heap, HeapSize, root):  # 在堆中做结构调整使得父节点的值大于子节点
        left = 2 * root + 1    #获得左下标
        right = left + 1       #获得右下标
        larger = root          #源点。
        if left < HeapSize and heap[larger] < heap[left]:
            larger = left
        if right < HeapSize and heap[larger] < heap[right]:
            larger = right
        print('取得左右子树中较大的large'+str(heap[larger]))
        if larger != root:  # 如果做了堆调整则larger的值等于左节点或者右节点的，这个时候做对调值操作
            heap[larger], heap[root] = heap[root], heap[larger]
            self.MAX_Heapify(heap, HeapSize, larger)

    def Build_MAX_Heap(self,heap):  # 构造一个堆，将堆中所有数据重新排序
        HeapSize = len(heap)  # 将堆的长度当独拿出来方便
        for i in range((HeapSize - 2) // 2, -1, -1):  # 从后往前出数，只要取一半。
            print('构建大顶堆时候的下标，就是从第一个非叶节点开始，从底下到上面'+str(i))
            self.MAX_Heapify(heap, HeapSize, i)


    '''
    推排序
    '''
    def HeapSort(self,heap):  # 将根节点取出与最后一位做对调，对前面len-1个节点继续进行对调整过程。
        self.Build_MAX_Heap(heap)  #构建大顶推
        print('构建的推是'+str(heap))
        for i in range(len(heap) - 1, -1, -1):
            print('#对掉头，尾顶点位置，然后调整')
            heap[0], heap[i] = heap[i], heap[0]  #对掉头，尾顶点位置，然后调整。
            print(' #开始调整。'+str(heap[0])+'        '+str(heap[i]))
            self.MAX_Heapify(heap, i, 0)
        return heap



    '''
    
    以下为插入排序，看看吧
    '''

    '''
    具体算法描述如下：

    1 从第一个元素开始，该元素可以认为已经被排序
    2 取出下一个元素，在已经排序的元素序列中从后向前扫描
    3 如果该元素（已排序）大于新元素，将该元素移到下一位置
    4 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
    5 将新元素插入到该位置后
    重复步骤2~5
    
    先来的直接插入排序
    '''
    def straight_sort(self, lists):
        # temp = lists[0]
        # lists.append[]
        for i in range(1, len(lists)):
            temp = lists[i]
            print('当前暂存变量为temp，哨兵的作用'+str(temp))
            j = i - 1
            while j > 0 and temp < lists[j] or j == 0  :
                print('开始交换')
                print(lists[j+1], lists[j])
                lists[j+1] = lists[j]
                # print('交换完的list'+str(lists))
                j -= 1
            lists[j+1] = temp
            print('交换完的list' + str(lists))
        return lists

    '''
    二分直接插入排序
    跟直接插入的排序仅仅就在于查找插入位置是二分法找。
    '''
    def  two_divide_straight_sort(self, lists):
        for i in range(1, len(lists)):
            temp = lists[i]
            print('当前暂存变量为temp，哨兵的作用'+str(temp))
            j = i - 1
            #插入二分查找法。二分法需要找到直接插入需要插入的位置
            left = 0
            right = i-1
            while left < right or left == right:
                mid = (right + left) // 2
                if temp < lists[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            print('找到要插入的的位置是'+str(left))
            print('将该位置之后的元素全部往后移动一位')
            for j in range(i-1, left-1,-1):
                print(lists[j+1], lists[j])
                lists[j+1] = lists[j]
                # print('交换完的list'+str(lists))
                j -= 1
            lists[left] = temp
            print('交换完的list' + str(lists))
        return lists


    '''
    希尔排序，看看
    先取一个小于n的整数d1作为第一个增量，把文件的全部记录分组。
    所有距离为d1的倍数的记录放在同一个组中。先在各组内进行直接插入排序；
    然后，取第二个增量d2<d1重复上述的分组和排序，直至所取的增量 
     =1(  <  …<d2<d1)，即所有记录放在同一组中进行直接插入排序为止。
    当增量减到1时，整个要排序的数被分成一组，排序完成。

    一般的初次取序列的一半为增量，以后每次减半，直到增量为1。
    '''

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
                temp = lists[i]
                while (j > 0  or j == 0) and lists[j] > temp  :
                    lists[j+h] = lists[j]
                    j = j - h
                lists[j + h] = temp
            h = (h-1) // 3  # 递减增量
            print('递减的增量变成了'+str(h))

        return lists

        #   quick _sort































testList=[4,3,7,5,10,2]
test = Solution()
test.merge(testList)