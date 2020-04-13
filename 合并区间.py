class Solution:
    def merge(self, intervals):
        if intervals is None:
            return []
        intervals.sort()#排序
        i=0
        while i <len(intervals)-1:
            if intervals[i][1]>=intervals[i+1][0]:#[i,j],[m,n] j与m比较，判断是否要合并
                if intervals[i][0]<intervals[i+1][0]:#i与m 比较
                    intervals[i+1][0]=intervals[i][0]
                if intervals[i][1]>intervals[i+1][1]:#j与n 比较
                    intervals[i+1][1]=intervals[i][1]
                del intervals[i]#合并后删除前一个
                i-=1
            i+=1
        return intervals
# 给出一个区间的集合，请合并所有重叠的区间。
#
# 示例 1:
#
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
