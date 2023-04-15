p = ")("

def balanced(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt = cnt + 1
        else:
            cnt = cnt - 1
        if cnt == 0:
            print(i, p[:i+1], p[i+1:])
            return p[:i+1], p[i+1:] #perfect

def right(p):
    tmp = []
    for i in p:
        if i == "(":
            tmp.append('(')
        elif len(tmp) > 0 and tmp[-1] == "(" and i==")":
            tmp.pop()
    if tmp == []:
        return True
    else:
        return False

def converse(u):
    tmp = u[1:-1]
    result = ""
    for i in tmp:
        if i == "(":
            result += ")"
        else:
            result += "("
    return result

def solution(p):
    result = ""
    if p == "" or right(p):
        return p
    u, v = balanced(p)
    if right(u):
        result = result + u + solution(v)
        return result
    else:
        result = "(" + solution(v) + ")" + converse(u)
        return result

print(solution(p))
