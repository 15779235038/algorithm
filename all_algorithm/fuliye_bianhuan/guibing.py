
#合并排序递归版本，





'''


分治函数，专门合并left，以及right

就是怎么把两个有序序列变成一个有序序列的工作。
'''
def merge(left, right):
    print()
    print('分治的left是'+str(left)+'分治的right'+str(right))

    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    if right:
        result += right

    print('合并排序结果为'+str(result))
    return result


def merge_sort(L):
    if len(L) <= 1:
        # When D&C to 1 element, just return it
        print('到叶子节点'+str(L)+'了')
        return L
    mid = len(L) // 2  #找中间位置
    left = L[:mid]       #中间位置的左边元素集合
    right = L[mid:]         #中间位置的右边元素集合
    print('主函数的left'+str(left))
    print('主函数的right' + str(right))



    print('插入之前是'+str(left))
    left = merge_sort(left)   #  将左边 的集合加入。
    print(' 左边集合是'+str(left))
    print('开始走向右边')
    right = merge_sort(right)    #  将右边集合
    print('右边集合是'+str(right))
    # conquer sub-problem recursively
    print('开始合并左右子树')
    return merge(left, right)
    # return the answer of sub-problem







#合并排序非递归版本

def merge_not(seq,low,mid,height):
    """合并两个已排序好的列表，产生一个新的已排序好的列表"""
    # 通过low,mid height 将[low:mid) [mid:height)提取出来
    left = seq[low:mid]
    right = seq[mid:height]
    print ('left:'+str(left)+ 'right:'+str(right) )

    k = 0   #left的下标
    j = 0   #right的下标
    result = [] #保存本次排序好的内容
    #将最小的元素依次添加到result数组中
    while k < len(left) and j < len(right):
        if left[k] <= right[j]:
            result.append(left[k])
            k += 1
        else:
            result.append(right[j])
            j += 1
    #将对比完后剩余的数组内容 添加到已排序好数组中
    result += left[k:]
    result += right[j:]
    #将原始数组中[low:height)区间 替换为已经排序好的数组
    seq[low:height] = result
    print ("seq:", seq)








if __name__ == "__main__":

    '''
    1
    '''
    # #递归方法去跑。
    # test = [1, 4, 2, 3.6, -1, 0, 25, -34, 8, 9, 1, 0]
    # print("original:", test)
    # print("Sorted:", merge_sort(test))


    '''
    2
    '''

    #非递归方法，两两合并
    seq = [5, 4, 3, 0, 1, 2, 7, 5, 11,9]
    i = 1
    while i < len(seq):
        print ('子数组 长度 : ',i)
        low = 0
        while low < len(seq):
            mid = low + i
            height = min(low + 2 * i, len(seq))
            if mid < height:
                print('low '+str(low)+'mid:'+str(mid)+'height:'+str(height))
                merge_not(seq,low,mid,height)
            low += 2*i
        i *= 2





