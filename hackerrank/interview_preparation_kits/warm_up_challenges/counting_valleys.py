#!/bin/python3

import os


# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

# Detailed commentary:
# https://broadleaf-hubcap-b1d.notion.site/Counting-Valleys-461d391cf14a463aaa110ac1b69ae1aa
def countingValleys(steps, path):
    altitude = 0
    prev_altitude = 0
    answer = 0

    for p in path:
        if p == 'U':
            altitude += 1
        else:
            altitude -= 1

        if altitude == 0:
            if prev_altitude < altitude:
                answer += 1
        prev_altitude = altitude

    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
