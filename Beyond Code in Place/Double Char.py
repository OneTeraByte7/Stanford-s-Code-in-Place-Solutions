"""Question :  Given string s. Return a new string that has 2 chars for every char in s"""

def double_char(s):
    result = ''
    for i in range(len(s)):
        result = result + s[i] + s[i]
    return result
