class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result=[]
        for cand in candies:
            result.append(cand+extraCandies>=max(candies))
        return result
