

#这个函数功能是将输入的list进行一次快速排序，根据传入的ios位置进行一次快排序。

#  输出这个排好的list以及ios到什么什么地方

def  swap(list_temp ,left ,right):
    temp = list_temp[left]
    list_temp[left] = list_temp[right]
    list_temp[right] = temp




#快速进行一次快速排序。
def  quick_change(lists, low, high, ios):
    while low < high:
        while lists[high] > lists[ios]:
            high -= 1
        swap(lists, high, ios)  #排序后记住这个ios位置。
        ios = high
        #交换list元素。
        while lists[low] < lists[ios]:
            low += 1
        swap(lists, low, ios)
        ios = low
    return lists, ios



quick_change( [34,12,46,45], 0, 3, 3)



import  random
def   findKthLarges(nums, k):

    if len(nums) == 0:
        return []
    low = 0
    high = len(nums) -1
    #随机生成一个位置，让这个nums快排，然后看这个位置的元素在什么地方，等于n-k，结束
    #大于n-k，往左边走。
    temp_nums = None
    new_position = None
    while 1:
        random_number = random.randint(low, high)
        # print('产生的随机数为'+str(random_number))
        #开始排序
        temp_nums, new_position = quick_change(nums,low,high,random_number)
        # print('查看结果'+str(temp_nums)+str(new_position))
        if new_position == len(nums) - k:
            # print('找到第k大元素')
            break
        elif new_position  >  len(nums) -k :
            # print('往左边走。')
            high = new_position - 1
        else:
            # print('往优走。')
            low = new_position + 1

    return temp_nums[new_position]

print(findKthLarges([34,12,46,45], 3))

