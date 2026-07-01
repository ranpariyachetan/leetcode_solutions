# https://leetcode.com/problems/process-string-with-special-operations-i/

def processStr(s: str) -> str:
    result = ""

    for c in s:
        if c == '*':
            result = result[:-1]
        elif c == '#':
            result += result
        elif c == '%':
            result = result[::-1]
        else:
            result += c

    return result


s = "a#b%*"
print(processStr(s))

s = "z*#"
print(processStr(s))