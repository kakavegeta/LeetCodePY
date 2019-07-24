class Solution:
    def minHeightShelves(self, books, shelf_width):
        dp = [0]*(len(books)+1)

        for i in range(1,len(books)+1):
            w, h = books[i-1][0], books[i-1][1]
            same_shelf_height = dp[i-1] + h
            dp[i] = same_shelf_height
            for j in range(i-1, 0, -1):
                w += books[j-1][0]
                if w > shelf_width:
                    break
                h = max(h, books[j-1][1])
                dp[i] = min(dp[i], dp[j-1]+h)
        return dp[len(books)]
                