class Solution:
    def insert(self, intervals, newInterval):
        intervals.append(newInterval) #加入队伍中，
        intervals.sort(key=lambda x: x[0])  #进行排序
        merged = [  ] #结果集合
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:  #反着来的枪框。
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1]= max(merged[-1][1], interval[1])
        return merged






test = Solution()
print(test.insert([[1, 3],[6,9]],[2,5]))

