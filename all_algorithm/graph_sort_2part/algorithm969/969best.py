class Solution:

    #煎饼翻转
    '''


    翻转失败了

    '''
    def pancakeSort(self, A):
        ans = []
        N = len(A)
        B = sorted(range(1, N+1), key = lambda i: -A[i-1])
        # print(B)
        for i in B:
            for f in ans:
                if i <= f:
                    i = f+1 - i
            ans.extend([i, N])
            N -= 1
        return ans

test = Solution()
print(test.pancakeSort([3,2,4,1]))

from  collections import  defaultdict
import  copy
class Solution1:
    #煎饼翻转
    '''
    先找到每个值的在数组应该在的位置，然后经过两个翻转。将其翻转过去

    首先找到最大值，两次翻转过去，然后次大。两次翻转。
    '''

    def pancakeSort1(self, A):
        ans = []
        N = len(A)
        B = copy.deepcopy(A)
        result =self.find_index(A)
        print('输出结果')

        index_ = len(A)
        for k, v in result.items():
            if B.index(v) == 0:
                ans.extend([index_])
            else:
                ans.extend([B.index(v) +1, index_ ])
            index_ -= 1
        return ans

    #寻找一个数组的元素排好序的下标。
    def find_index(self, A):
        # print(A)
        position = defaultdict(int)
        for j in range(len(A)-1, -1,  -1):
            max = 0
            index = 0
            for i in range(0, len(A)):
                if A[i] > max:
                    max = A[i]
                    index = i
            position[j] = max
            A[index] = min(A)-1
        print(position)
        return  position   #字典保存的从大到小的每个元素简直对
    #其中键为位置，值为数组的值




test = Solution1()
print(test.pancakeSort1(  [3,2,4,1]))











