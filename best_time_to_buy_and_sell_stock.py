class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0;
        
        B,S = [0]*len(prices),[0]*len(prices);
        low,high = prices[0],prices[-1]
        
        for k in range(len(prices)):
            low = min(low,prices[k])
            B[k] = low;
            high = max(high,prices[-k-1])
            S[-k-1] = high;
        return max([S[i]-B[i] for i in range(len(prices))])
