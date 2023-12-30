###给定一个字符串string = "Hello, World!"，请统计字符串中每个字符的出现次数，并将结果存储在一个字典中。

stringhello = "Hello, World!"
char_count = {}

for char in stringhello:
    if char not in char_count:
        char_count[char] = 1
    else:
        char_count[char]+=1

print(char_count)
