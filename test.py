import requests
import re

url = 'https://www.gushiwen.org/'

try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    text = r.content
    # print(text)
    res = re.findall(r'(?<=<div class="sons">).*(?=</textarea></div>)', r.text)
    print(res)

except Exception as e:
    print("爬取失败: " + e)

# with open('test.html', 'w', encoding='utf-8') as fw:
#     fw.write(r.text)

"""
# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print("{}x{}={}\t".format(j, i, i * j), end=' ')
    print()
"""

# people = {}
# for x in range(1, 31):
#     people[x] = 1
# # print(people)
# check = 0
# i = 1
# j = 1
# while i <= 31:
#     if i == 31:
#         i = 1
#     elif j == 16:
#         break
#     else:
#         if people[i] == 0:
#             i += 1
#             continue
#         else:
#             check += 1
#             if check == 9:
#                 people[i] = 0
#                 check = 0
#                 print("{}号下船了".format(i))
#                 j += 1
#             else:
#                 i += 1
#                 continue
