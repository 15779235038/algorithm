def two_divide_straight_sort(lists):


    '''

    二分插入排序
    :param lists:
    :return:
    '''
    for i in range(1, len(lists)):
        temp = lists[i]
        print('当前暂存变量为temp，哨兵的作用' + str(temp))
        j = i - 1
        # 插入二分查找法。二分法需要找到直接插入需要插入的位置
        left = 0
        right = i - 1
        while left < right or left == right:
            mid = (right + left) // 2
            if temp + lists[mid] < lists[mid] + temp:
                right = mid - 1
            else:
                left = mid + 1

        print('找到要插入的的位置是' + str(left))
        print('将该位置之后的元素全部往后移动一位')
        for j in range(i - 1, left - 1, -1):
            print(lists[j + 1], lists[j])
            lists[j + 1] = lists[j]
            # print('交换完的list'+str(lists))
            j -= 1
        lists[left] = temp
        print('交换完的list' + str(lists))
    return lists

class Solution:
    def largestNumber(self,nums):
        resulst = two_divide_straight_sort([str(i) for i in nums])
        print(resulst[::-1])
        best_result = ""
        for j in resulst[::-1]:
            best_result = best_result + j
        return "0" if best_result[0] == "0" else best_result



test = Solution()
test.largestNumber([3,30,34,5,9])