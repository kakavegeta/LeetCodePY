from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: 'str', words: 'List[str]') -> 'str':
        Map = Counter(list(filter(lambda x: x.isalpha(), licensePlate.lower())))
        minlen, ret = 16, ''
        for word in words:
            if self.match(word, Map):
                if minlen > len(word):
                    ret = word
                    minlen = len(word)
                    print(ret, minlen)
        return ret
    
    def match(self, word, Map):
        count = Counter(list(filter(lambda x: x.isalpha(), word.lower())))
        for char in Map.keys():
            if count[char]<Map[char]:
                return False
        return True


if __name__ == "__main__":
    plate = "1s3 PSt"
    words = ["step","steps","stripe","stepple"]
    sol = Solution()
    ret = sol.shortestCompletingWord(plate, words)
    print(ret)
