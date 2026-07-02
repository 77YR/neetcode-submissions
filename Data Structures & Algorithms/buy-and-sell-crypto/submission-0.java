class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int curProfit = Integer.MIN_VALUE;
        int buy = Integer.MAX_VALUE, sell = Integer.MIN_VALUE;
        for (int val : prices){
                sell = val;
            if (val < buy)
                buy = val;

            curProfit = sell - buy;
            profit = Math.max(profit, curProfit);
        }
        return profit;
    }
}
