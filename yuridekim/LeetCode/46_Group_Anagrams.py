class Solution(object):
    def enumerateChar(self, word):
        char_arr = [0] * 26
        for char in word:
            char_arr[ord(char)- 97] += 1
        return char_arr
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        enum_arr = [self.enumerateChar(strs[0])]
        result_list = [[strs[0]]]
        del strs[0]
        for str in strs:
            str_arr = self.enumerateChar(str)
            if str_arr in enum_arr:
                result_list[enum_arr.index(str_arr)].append(str)
            else:
                enum_arr.append(str_arr)
                result_list.append([str])
        return result_list