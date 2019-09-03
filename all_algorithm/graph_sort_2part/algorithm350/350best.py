from  collections import  defaultdict
class Solution:
    def intersect(self, nums1, nums2):

        if not len(nums1) or  not len(nums2):
            return []
        ans = []
        has_dict = defaultdict(int)
        for i in nums1:
            has_dict[i] += 1

        for j in nums2:
            if  has_dict.get(j): #有这个数
                # while has_dict[j] > 0:
                     ans.append(j)
                     has_dict[j] -= 1
        return ans

    #拓展，两个有序数组如何求交集

    '''
    假设两个数组 a 和 b，a 的长度为 m ，b 的长度为 n ， m < n， 有以下四种解法：

（1）每次从数组 b 中 取一个数，遍历 a 中所有元素进行比较，若相同就保存，这样时间复杂度为O(m*n)； 
（2）由于数组是有序的，每次从数组 b 中 取一个数，对 a 中元素进行二分查找，若相同就保存，时间复杂度为O(nlog(m))； 
（3）将 a 中的元素 hash 存储（用map或者dict），遍历 b 中的每一个值看是否在这个hash 中，若存在就保存，时间复杂度是 O(m)，空间复杂度是O(n)； 
（4）a 和 b 两个数组的头部分别维护两个指针，若其中一个比另一个小，则向前移动，若遇到相等时保存，遍历直到其中一个数组的尾部，时间复杂度O(m+n)；
————————————————

    
    '''







test = Solution()
print(test.intersect([1,2,2,1], [2,2]))