from  collections  import  defaultdict
class Solution:
    #求交集
    def intersection(self, nums1, nums2):
        has_dict = defaultdict(int)
        result = []
        for i in nums1:
            if has_dict.get(i) is not None:
                nums1[i] = 1
        #0  1#  2#  3#  4#  5#
        for j in nums1:
            if has_dict.get(j) is not None:
                has_dict[j] = None
                result.append(j)
        return result




