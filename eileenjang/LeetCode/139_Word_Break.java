class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        int N = s.length();
        boolean[] DP = new boolean[N + 1];
        DP[0]=true;
        
        for (int i = 1; i <= N; i++){ 
            for (int j = 0; j < i; j++){ 
                if (DP[j] && wordDict.contains(s.substring(j,i))) {
                    DP[i] = true;
                    break;
                }
            }
        }
        
        return DP[N];
           
    }
}
