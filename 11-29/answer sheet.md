# 11 月 29 日上机报告

王禹东 2020050901021

1. if i == 'AAA' or i == 'uestc' or i == 'BBB':
2. if x == s[i:i+len(x)]:
3. s=s[:i]+t+s[i+len(x)+1:]
4. if s[i] != s[len(s) - (i + 1)]:
5. i = chr(ord(i[0]) - 32) + i[1:]
6. 如下

```python
key = int(input('key='))
word = input('word=')
t = ''
for character in word:
    if 96 < ord(character) < 123 - key or 64 < ord(character) < 91 - key:
       new_char = chr(ord(character) + key)
    else:
        new_char = chr(ord(character) - 26 + key)
    t += new_char
print(t)
```
