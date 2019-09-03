
class Solution:
    def wiggleSort(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(reverse=True)
        mid = len(nums) // 2
        print(nums)
        nums[1::2],nums[0::2] = nums[:mid], nums[mid:]

        return nums


test = Solution()
print(test.wiggleSort([32,3,2,1,4,3,5]))