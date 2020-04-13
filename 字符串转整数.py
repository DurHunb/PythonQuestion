class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        sett = ['+', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        i = 0

        # 注意空字符不要写成'',应该是' '
        # 先把指针移到第一个非空字符
        while i < len(str) and str[i] == " ":
            i += 1
        if i == len(str): return 0
        if str[i] not in sett: return 0

        # 对第一个非空字符分情况讨论：
        # 一类是以+，-开头；
        # 一类是以数字开头；
        flag = 1
        if str[i] == '+' or str[i] == '-':
            if str[i] == "-": flag = -1
            i += 1
            if i >= len(str): return 0  # 超出范围
            # 如果第一个数是+或者-，但是下一个数不是数字，不满足要求，return 0
            if str[i] not in sett[2:]: return 0

            # 开始读数
        x = 0
        while i < len(str) and str[i] in sett[2:]:
            x = x * 10 + int(str[i])
            i += 1
        x *= flag

        # 判断是否溢出
        if flag > 0:
            return x if x <= INT_MAX else INT_MAX
        else:
            return x if x >= INT_MIN else INT_MIN
        # 说明：
        #
        # 假设我们的环境只能存储32位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，请返回  INT_MAX(231 − 1) 或 INT_MIN(−231) 。
        #
        # 示例 1:
        #
        # 输入: "42"
        # 输出: 42
        # 示例 2:
        #
        # 输入: "   -42"
        # 输出: -42
        # 解释: 第一个非空白字符为'-', 它是一个负号。我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 - 42 。
        
        # 示例 3:
        #
        # 输入: "4193 with words"
        # 输出: 4193
        # 解释: 转换截止于数字
        # '3' ，因为它的下一个字符不为数字。
        # 示例 4:
        #
        # 输入: "words and 987"
        # 输出: 0
        # 解释: 第一个非空字符是
        # 'w', 但它不是数字或正、负号。
        # 因此无法执行有效的转换。
        # 示例 5:
        #
        # 输入: "-91283472332"
        # 输出: -2147483648
        # 解释: 数字
        # "-91283472332"
        # 超过
        # 32
        # 位有符号整数范围。
        #      因此返回
        # INT_MIN(−231) 。

