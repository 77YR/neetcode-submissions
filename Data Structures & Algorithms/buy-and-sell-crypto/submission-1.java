class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int buy = Integer.MAX_VALUE;
        for (int val : prices){
                int sell = val;
            if (val < buy)
                buy = val;
            profit = Math.max(profit, (sell - buy));
        }
        return profit;
    }
}
