class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        min_price = prices[0]
        

        for i in range(len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            currProfit = prices[i] - min_price
            if currProfit > profit:
                profit = currProfit
            print(min_price)
            print(currProfit)


        return profit



            


        
        