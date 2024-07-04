"""Question : Given a string s, return a new string made of the chars from s, whenever the chars in s are exactly 'c' 'a' or 't' (not case sensitive). """

def catty(s):
    result = ''
    for i in range(len(s)):
        low = s[i].lower()
        if low == 'c' or low == 'a' or low == 't':
            result += s[i]  
    return result
