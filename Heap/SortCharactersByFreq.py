import heapq
class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}
        pq, res = [], ''
        for c in s:
            if c not in freq:
                freq[c] = 1
            else:
                freq[c] += 1
        for key, value in freq.items():
            heapq.heappush(pq,(-value, key))
        while pq:
            print(pq)
            e = heapq.heappop(pq)
            count = freq[e[-1]]
            print(count)
            for _ in range(count):
                res += e[-1]
        return res 
    
    def frequencySort2(self, s):
        freq = {}
        res = ''
        for c in s:
            if c not in freq:
                freq[c] = 1
            else:
                freq[c] += 1
        newfreq = sorted(freq, key=lambda x:-freq[x])
        for key in newfreq:
            res += key * freq[key] 
        return res

def main():
    s = 'tree'
    sol = Solution()
    print(sol.frequencySort2(s))

if __name__ == "__main__":
    main()
