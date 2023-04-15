from itertools import permutations

def check(users, banned):
    for i in range(len(banned)):        
        if len(banned[i]) != len(users[i]):
            return False
        else:
            for j in range(len(banned[i])):
                if banned[i][j] != '*' and banned[i][j] != users[i][j]:
                    return False
    return True

banned_id = ["*rodo", "*rodo", "******"]
user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]


def solution(user_id, banned_id):
    user_permutation = list(permutations(user_id, len(banned_id)))
    # print(user_permutation)
    ban_set = []

    for users in user_permutation:
        if not check(users, banned_id):
            continue
        else:
            users = set(users)
            if users not in ban_set:
                ban_set.append(users)

    return len(ban_set)

print(solution(user_id, banned_id))
