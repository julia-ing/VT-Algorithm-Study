class Solution(object
  def longestPalindrome(self, s):):
    ## Second Try : replace slicing (Runtime: 455 ms)
    # case 1. Two consecutive characters are equal
    # case 2. Both sides of a character are euqal
    
    def find_longest(l, r):
      while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
      return s[l + 1:r]

    longest = ''
    for i in range(len(s)):
      # case 1.
      s1 = find_longest(i, i)
      if len(s1) > len(longest): longest = s1

      #case 2.
      s2 = find_longest(i, i + 1)
      if len(s2) > len(longest): longest = s2

    return longest


'''
# First try : Brute force (Runtime: 6296 ms)
class Solution(object):
    def longestPalindrome(self, s):
        ## leverage s[::-1] (flipping the word)

        if s == s[::-1] or len(s) == 1:
            return s

        longest = ''
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                word = s[i:j]
                if len(word) < len(longest):
                    continue
                if word == word[::-1]:
                        longest = word
        return longest
'''
