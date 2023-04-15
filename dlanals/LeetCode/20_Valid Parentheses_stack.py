class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_dic = {')':'(', ']':'[', '}':'{'}
        for bracket in s:
            if bracket in bracket_dic.values():
                stack.append(bracket)
            else:
                if len(stack) == 0 : return False
                else:
                    if stack.pop() == bracket_dic[bracket]: continue
                    else: return False

        if len(stack) == 0 : return True
        else: return False
        
# 예외처리 좀 더 깔끔한 
class Solution(object):
    def isValid(self, s):
        opcl = dict(('()', '[]', '{}'))
        stack = []
        
        for idx in s:
            if idx in '([{':
                stack.append(idx)
            elif len(stack) == 0 or idx != opcl[stack.pop()]:
                return False
        # At last, we check if the stack is empty or not...
        # If the stack is empty it means every opened parenthesis is being closed and we can return true, otherwise we return false...
        return len(stack) == 0
