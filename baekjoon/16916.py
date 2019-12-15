from sys import stdin

S = stdin.readline().strip('\n')
P = stdin.readline().strip('\n')

BASE = 256
PRIME = 127

p_len = len(P)
s_len = len(S)


def hash_next_string(idx, prev_hashed):
    if idx + p_len >= s_len:
        return

    char_to_remove = S[idx-1]
    string = S[idx:idx+p_len]
    value_to_sub = (ord(char_to_remove) * pow(BASE, p_len - 1)) % PRIME

    result = (((prev_hashed - value_to_sub) * BASE) % PRIME + ord(string[-1])) % PRIME
    return result


def hash_string(string):
    result = 0
    for i in range(1, p_len):
        result = (result + ord(string[i-1])) * BASE % PRIME
    result += ord(string[-1])

    return result % PRIME


def match():
    hashed_p = hash_string(P)
    hashed_s = hash_string(S[0:p_len])

    for i in range(0, s_len - p_len + 1):
        if hashed_p == hashed_s:
            if S[i:i+p_len] == P:
                return 1
        else:
            hashed_s = hash_next_string(i + 1, hashed_s)
    return 0


print(match())
