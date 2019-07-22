class Solution:
    def minHeightShelves(self, books, shelf_width):
        dp = [float('inf')]*len(books)
        for i in range(len(books)):
            w, h = books[i][0], books[i][1]
            same_shelf_height = dp[i-1] + h
            for j in range(i-1, -1, -1):
                w += books[j][0]
                if w > shelf_width:
                    break
                h = max(h, books[j][1])
                dp[i] = max(same_shelf_height, dp[j-1]+h)
        return dp[len(books)]
                