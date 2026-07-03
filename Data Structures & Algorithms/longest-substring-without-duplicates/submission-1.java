class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> set = new HashSet<Character>();
        int l = 0, r = 0;
        int length = 0;

        while (l <= r && r < s.length()){
            set.add(s.charAt(l));
            set.add(s.charAt(r));
            
            if (set.size() == (r - l + 1)){
                r++;
            }
            else{
                set.remove(s.charAt(l));
                l++;
            }

            length = Math.max(length, r - l);
        }
        return length;
    }
}
