class Solution:


    '''

    我们首先对这些车辆按照它们的起始位置降序排序，并且用 (target - position) / speed
    计算出每辆车在不受其余车的影响时，行驶到终点需要的时间。对于相邻的两辆车 S 和 F，
    F 的起始位置大于 S，如果 S 行驶到终点需要的时间小于等于 F，那么 S 一定会在终点
    前追上 F 并形成车队。这是因为在追上 F 之前，S 的行驶速度并不会减小，而 F 却有
    可能因为追上前面的车辆而速度减小，因此 S 总能在终点前追上 F。

    '''




    def two_divide_straight_sort(self, lists):
            for i in range(1, len(lists)):
                temp = lists[i]
                print('当前暂存变量为temp，哨兵的作用' + str(temp))
                j = i - 1
                # 插入二分查找法。二分法需要找到直接插入需要插入的位置
                left = 0
                right = i - 1
                while left < right or left == right:
                    mid = (right + left) // 2
                    if temp[0] > lists[mid][0]:
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



    def carFleet(self, target, position, speed):

        car_speed = []
        for car, speeds in zip(position, speed):
            car_speed.append([car, speeds])

        car_speed_dis = [[i,j,12-i]for i,j in car_speed]
        print(car_speed_dis)
        self.two_divide_straight_sort(car_speed_dis)
        print(car_speed_dis) #[position,speed,dis]
        #怎么搞定，两两比对，如果小于某个距离，就合并，不然就。重新一个【】


        print(car_list)



test = Solution()

test.carFleet(12,[10,8,0,5,3], [2,4,1,1,3])


