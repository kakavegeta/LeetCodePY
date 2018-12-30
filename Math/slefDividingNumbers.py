class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for num in range(left, right+1):
            count = 0
            string = str(num)
            for i in string:
                if i=='0' or num%int(i)!=0:
                    count += 1
                    break
            if count == 0:
                res.append(num)
        return res





if __name__ == "__main__":
    sol = Solution()
    print(sol.selfDividingNumbers(1,22))
