class Solution:
    #荷兰国旗问题
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        #首先需要找到边界点。
        #初始化3个指针
        i = 0   # And i is the boundary for the numbers less than the mid value.  0的最右位置
        j = 0  # j is the position of the number under consideration.当前下标
        n = len(nums) -1  #n holds the lower boundary of numbers greater than mid. 2的最左位置
        while j < n or j ==n :
            #从右向左扫描
            if nums[j] < 1:
                nums[i], nums[j] = nums[j],nums [i]
                i += 1
                j += 1
            elif nums[j] > 1:
                nums[j], nums[n] = nums[n], nums[j]
                n -= 1
            else:
                j += 1
        return nums


      #问题拓展，如果有超过3色。那么这里的1就是硬编码，了，那怎么办？
    def sortColors_update(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_sets = set(nums)
        color_number = len(nums_sets)   #颜色个数。
        #统计不同颜色出来，

        i = 0  # And i is the boundary for the numbers less than the mid value.  0的最右位置
        j = 0  # j is the position of the number under consideration.当前下标
        n = len(nums) - 1  # n holds the lower boundary of numbers greater than mid. 2的最左位置
        while j < n or j == n:
            # 从右向左扫描
            if nums[j] < 1:  #跟1的关系，决定j在哪里，多种颜色。这里的1就要变了。
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] > 1:
                nums[j], nums[n] = nums[n], nums[j]
                n -= 1
            else:
                j += 1
        return nums


test = Solution()
print(test.sortColors([1, 2, 0, 2, 1, 2, 1, 1, 1, 0]))

