class Solution:
    def maxSumDivThree(self, nums) :
        l1 = sorted([x for x in nums if x % 3 == 1])
        l2 = sorted([x for x in nums if x % 3 == 2])

        total = sum(nums)
        if total % 3 == 0:
            return total
        elif total % 3 == 1:
            ans = 0
            if len(l1) > 0:
                ans = max(ans, total - l1[0])
            if len(l2) >= 2:
                ans = max(ans, total - l2[0] - l2[1])
            return ans

        else:
            ans = 0
            if len(l2) > 0:
                ans = max(ans, total - l2[0])
            if len(l1) >= 2:
                ans = max(ans, total - l1[0] - l1[1])
            return ans

