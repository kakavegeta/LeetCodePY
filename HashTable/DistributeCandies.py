class Solution:
    def distributeCandies(self, candies: 'List[int]') -> 'int':
        num = len(candies)//2
        candy_set = set(candies)
        return min(len(candy_set), num)


