class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ra, ia = a.split('+')
        rb, ib = b.split('+')
        r_res = int(ra)*int(rb) - int(ia[:-1])*int(ib[:-1])
        i_res = int(ra)*int(ib[:-1]) + int(rb)*int(ia[:-1])
        return str(r_res) + '+' + str(i_res) + 'i'

if __name__ == "__main__":
    sol = Solution()
    print(sol.complexNumberMultiply('1+-1i','1+-1i'))