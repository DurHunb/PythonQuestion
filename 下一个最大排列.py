class Solution:
    def nextPermutation(self, nums) :
        n=len(nums)
        flag=True
        for i in range(n-1,0,-1):#逆序
            if nums[i]>nums[i-1]:#如果右边大于左边
                flag=False
                nums[i:]=sorted(nums[i:])#从右边一直往右排序
                for j in range(i,n):
                    if nums[i-1]<nums[j]:#在右边一列数中，找到第一个大于左边的数，交换
                        nums[i-1],nums[j]=nums[j],nums[i-1]
                        break
                return nums
        if flag:
            return nums.reverse()

        # 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
        #
        # 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
        #
        # 必须原地修改，只允许使用额外常数空间。
        #
        # 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
        # 1, 2, 3 → 1, 3, 2
        # 3, 2, 1 → 1, 2, 3
        # 1, 1, 5 → 1, 5, 1