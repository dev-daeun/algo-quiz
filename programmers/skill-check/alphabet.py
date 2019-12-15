def solution(s):
    split_s = list(s)
    result = list()

    idx = 0
    for i in range(len(split_s)):
        if split_s[i] == ' ':
            idx = 0
            result.append(split_s[i])
        else:
            if idx % 2 == 0:
                result.append(split_s[i].upper())
            else:
                result.append(split_s[i].lower())
            idx += 1

    return ''.join(result)
