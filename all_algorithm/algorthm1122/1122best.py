class Solution:
    def relativeSortArray(self, arr1, arr2):

        #就是用一个大数组，利用下标。
       arr = [0 for _ in range(1001)]
       ans  = []
       for i in arr1:
           arr[i] += 1

       for  j  in  arr2:
           while  arr[j] !=0:
               ans.append(j)
               arr[j] -= 1

       for  k  in range(0,len(arr)):
           while arr[k] > 0:
               ans.append(k)
               arr[k] -=1
       return  ans




