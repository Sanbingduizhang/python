# coding:utf-8
import urllib.request

page = urllib.request.urlopen('http://tieba.baidu.com/p/1753935195')
for line in page:
    line = line.decode('utf-8')
    print(line)
# htmlcode = page.read()
#
# with open('test.txt', 'a+') as fw:
#     fw.write(str(htmlcode))
