class Solution:
    def sortArrayByParityII(self, A):

        j = 1
        for i  in range(0,len(A),2):
            if A[i] % 2:
                while A[j] % 2 :
                      j += 2
                A[i], A[j] = A[j] ,A[i]

        return A

test= Solution()
print(test.sortArrayByParityII([2,3,5,34,2,432,234]))
