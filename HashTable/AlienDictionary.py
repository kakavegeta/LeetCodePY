class Solution:
    def isAlienSorted(self, words, order):
        m = {c: i for i, c in enumerate(order)}
        for i in range(len(words)-1):
            if not self.compare(words[i], words[i+1], m):
                return False
        return True
    
    def compare(self, s1, s2, m):
        len1, len2 = len(s1), len(s2)
        for i in range(min(len1,len2)):
            if m[s1[i]] > m[s2[i]]:
                return False
            elif m[s1[i]] == m[s2[i]]:
                if len1>len2:
                    return False
            else:
                return True






        