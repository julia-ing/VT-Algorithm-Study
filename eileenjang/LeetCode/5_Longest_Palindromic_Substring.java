class Solution {
    public String longestPalindrome(String s) {
        String max = "";
        for (int i = 0; i < s.length(); i++) {
            String str1 = checkPalind(s, i, i);
            String str2 = checkPalind(s, i, i + 1);

            if (str1.length() > max.length() && str1.length() >= str2.length()) {
                max = str1;
            }
            if (str2.length() > max.length() && str1.length() < str2.length()) {
                max = str2;
            }
        }
        return max;
    }
    
  public String checkPalind(String s, int left, int right) {
    while (left >= 0 && right < s.length()) {
      if (s.charAt(left) == s.charAt(right)) {
        left--;
        right++;
      } else {
          break;
      }
    }
    left++;
    right--;
    return s.substring(left, right + 1);
  }
}
