from sys import stdin

S = stdin.readline().strip('\n')
P = stdin.readline().strip('\n')

BASE = 256
PRIME = 127


def hash_next_string(idx, prev_hashed):
    p_len = len(P)

    char_to_remove = S[idx-1]
    string = S[idx:idx+p_len]
    value_to_sub = (ord(char_to_remove) * pow(BASE, p_len - 1)) % PRIME

    result = (((prev_hashed - value_to_sub) * BASE) + ord(string[-1])) % PRIME
    return result


def hash_string(string):
    p_len = len(P)

    result = 0
    for i in range(1, p_len):
        result = (result + ord(string[i-1])) * BASE
    result += ord(string[-1])

    return result % PRIME


def match():
    hashed_p = hash_string(P)

    p_len = len(P)
    s_len = len(S)
    hash_list = [hash_string(S[0:p_len])]

    for i in range(0, s_len - p_len + 1):
        if i == 0:
            if hash_list[0] == hashed_p:
                if S[0:p_len] == P:
                    return 1
        else:
            hashed_str = hash_next_string(i, hash_list[i-1])
            if hashed_str == hashed_p:
                if S[i:i+p_len] == P:
                    return 1
            hash_list.append(hashed_str)

    return 0


print(match())
