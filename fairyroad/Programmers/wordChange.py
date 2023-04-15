def similarity_check(begin, target):
    cnt = 0
    for i in range(len(begin)):
        if begin[i] != target[i]:
            cnt = cnt + 1
    return cnt

def words_1(words, begin):
    for i in words:
        if similarity_check(begin, i) == 1:
            return i
        
words = ["hot", "dot", "dog", "lot", "log"]
begin = "hit"
target = "cog"
cnt = 0

def solution(begin, target, words):
    cnt = 0
    if target not in words:
        return 0
    while True:
        cnt = cnt + 1
        if similarity_check(begin, target) <= 1:
            return cnt
        else:
            change = words_1(words, begin)
            words.remove(change)
            begin = change
print(solution(begin, target, words))
