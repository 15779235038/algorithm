

#动态规划思想

def   best_sum(lists):
     sum = 0
     ans = lists[0]
     for i  in  lists:
         temp =  sum + i
         if sum >  temp:   #没有效果
            pass
         else:        #有效果
             sum += i


         ans = max(ans, sum)
         print(ans)

     return ans



#分治法，求最大子序和

class Solution(object):
    def maxSubArray(self, nums):
        # 主函数
        left = 0
        # 左右边界
        right = len(nums) - 1
        # 求最大和
        maxSum = self.divide(nums, left, right)
        return maxSum




    def divide(self, nums, left, right):
        # 如果只有一个元素就返回
        if left == right:
            return nums[left]
        # 确立中心点
        center = (left + right) // 2
        print ("center是多少呢"+str(center))
        # 求子序在中心点左边的和
        leftMaxSum = self.divide(nums, left, center)
        print('leftMaxSum'+str(leftMaxSum))
        # 求子序在中心点右边的和
        rightMaxSum = self.divide(nums, center + 1, right)

        print('rightMaxSum' + str(rightMaxSum))

        # 求子序横跨2边的和，分成左边界和和右边界和
        leftBorderSum = nums[center]
        leftSum = nums[center]
        for i in range(center - 1, left - 1, -1):
            leftSum += nums[i]
            if leftSum > leftBorderSum:
                # 不断更新左区块的最大值
                leftBorderSum = leftSum



        print('leftBorderSum' +str(leftBorderSum))


        rightBorderSum = nums[center + 1]
        rightSum = nums[center + 1]
        for i in range(center + 2, right + 1):
            rightSum += nums[i]
            if rightSum > rightBorderSum:
                # 不断更新右区块的最大值
                rightBorderSum = rightSum
        # 左边界的和 + 右边那块的和
        print('右边边界的最大值' +str(rightBorderSum))

        BorderSum = leftBorderSum + rightBorderSum

        print('中间边界之最大值'+str(BorderSum))
        return max(leftMaxSum, rightMaxSum, BorderSum)


lists = [-2, 3, -1 ,1, 4, -3]

test = Solution()
test.maxSubArray(lists)

# print(best_sum(lists))

