from collections import Counter


def repeatedString(s, n):
    return Counter(s)['a'] * (n // len(s)) + Counter(s[:n % len(s)])['a']
