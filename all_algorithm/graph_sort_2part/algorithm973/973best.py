class Solution:
    def kClosest(self, points, K):
        #利用快排，随机找一个点，然后如果该点进行快排一次，如果该点在位置k，就把该位置前面元素返回
        points.sort(key=lambda P: P[0] ** 2 + P[1] ** 2)
        return points[:K]



