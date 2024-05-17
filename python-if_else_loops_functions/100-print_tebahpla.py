#!/usr/bin/python3
for i in range(26):
    result = ""
    if i % 2 == 0:
        result = chr(ord('z') - i)
    else:
        result = chr(ord('Z') - i)
    print("{}".format(result), end="")
