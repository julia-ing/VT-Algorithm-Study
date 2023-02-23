class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        int index = 0;
        int max = 0;
        int prev = 0;

        Set<Character> set = new HashSet<>();
        
        while (index < s.length()) {
            char c = s.charAt(index);
            if(!set.contains(c)) {
                set.add(c);
                index++;
                max = Math.max(set.size(), max);
            }
            else {
                set.remove(s.charAt(prev));
                prev++;
            }
        }
        return max;
    }
}
